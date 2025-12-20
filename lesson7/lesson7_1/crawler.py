import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
import pandas as pd
import requests
from bs4 import BeautifulSoup

SCHEMA = {
    "name": "匯率資訊",
    "baseSelector": "table[title='牌告匯率'] tr",
    "fields": [
        {"name": "幣別", "selector": "td[data-table='幣別'] div.print_show", "type": "text"},
        {"name": "本行即期買入", "selector": "td[data-table='本行即期買入']", "type": "text"},
        {"name": "本行即期賣出", "selector": "td[data-table='本行即期賣出']", "type": "text"}
    ]
}


async def _fetch_async():
    strategy = JsonCssExtractionStrategy(SCHEMA)
    run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, extraction_strategy=strategy)
    async with AsyncWebCrawler() as crawler:
        url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
        result = await crawler.arun(url=url, config=run_config)
        data = json.loads(result.extracted_content)
        return data


def _run_async(coro_func, *args, **kwargs):
    """Run an async coroutine function in a fresh event loop.

    Accepts a coroutine *function* (not an already-created coroutine object)
    to avoid "cannot reuse already awaited coroutine" errors.
    """
    # Ensure we call the function to create a fresh coroutine each time
    coro = coro_func(*args, **kwargs)
    try:
        return asyncio.run(coro)
    except NotImplementedError:
        # On some environments (embedded event loop) try selector policy then retry
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except Exception:
            pass
        return asyncio.run(coro_func(*args, **kwargs))


def fetch_exchange_rates_raw():
    """Fetch exchange rates and return a cleaned pandas.DataFrame.

    Replaces empty buy/sell with '暫停交易' and filters out rows where both are unavailable.
    """
    # Try primary async fetch (uses Playwright). On failure, fall back to requests+BS4.
    try:
        data = _run_async(_fetch_async)
    except Exception:
        # Fallback: synchronous HTTP fetch and parse with BeautifulSoup
        try:
            url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
            resp = requests.get(url, timeout=10)
            resp.encoding = resp.apparent_encoding
            html = resp.text
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.select_one("table[title='牌告匯率']")
            rows = []
            if table:
                for tr in table.select('tr'):
                    try:
                        cur = tr.select_one("td[data-table='幣別'] div.print_show")
                        buy = tr.select_one("td[data-table='本行即期買入']")
                        sell = tr.select_one("td[data-table='本行即期賣出']")
                        if cur is None:
                            continue
                        row = {
                            '幣別': cur.get_text(strip=True),
                            '本行即期買入': buy.get_text(strip=True) if buy else '',
                            '本行即期賣出': sell.get_text(strip=True) if sell else ''
                        }
                        rows.append(row)
                    except Exception:
                        continue
            data = rows
        except Exception:
            # If fallback also fails, re-raise the original exception
            raise
    df = pd.DataFrame(data)

    if df.empty:
        return df

    # Normalize whitespace and replace empty with NaN then '暫停交易'
    df['本行即期買入'] = df.get('本行即期買入', '').astype(str).str.strip()
    df['本行即期賣出'] = df.get('本行即期賣出', '').astype(str).str.strip()

    df['本行即期買入'] = df['本行即期買入'].replace({'': None}).fillna('暫停交易')
    df['本行即期賣出'] = df['本行即期賣出'].replace({'': None}).fillna('暫停交易')

    # Filter out rows where both buy and sell are '暫停交易'
    df = df[~((df['本行即期買入'] == '暫停交易') & (df['本行即期賣出'] == '暫停交易'))]

    # Reset index for nicer display
    df = df.reset_index(drop=True)
    return df
