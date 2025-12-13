import streamlit as st
import asyncio
import json
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy
from datetime import datetime, timedelta

# 匯率爬取 schema
SCHEMA = {
    "name": "匯率資訊",
    "baseSelector": "table[title='牌告匯率'] tr",
    "fields": [
        {"name": "幣別", "selector": "td[data-table='幣別'] div.print_show", "type": "text"},
        {"name": "本行即期買入", "selector": "td[data-table='本行即期買入']", "type": "text"},
        {"name": "本行即期賣出", "selector": "td[data-table='本行即期賣出']", "type": "text"}
    ]
}

@st.cache_data(ttl=600, show_spinner=False)
def fetch_rates():
    async def _fetch():
        strategy = JsonCssExtractionStrategy(SCHEMA)
        run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, extraction_strategy=strategy)
        async with AsyncWebCrawler() as crawler:
            url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
            result = await crawler.arun(url=url, config=run_config)
            data = json.loads(result.extracted_content)
            return data
    return asyncio.run(_fetch())

def get_valid_rates(data):
    # 過濾無法交易的貨幣（買入或賣出皆為空）
    valid = []
    for row in data:
        buy = row.get("本行即期買入", "").strip()
        sell = row.get("本行即期賣出", "").strip()
        if buy == '' and sell == '':
            continue
        row["本行即期買入"] = buy if buy else "暫停交易"
        row["本行即期賣出"] = sell if sell else "暫停交易"
        valid.append(row)
    return valid

def main():
    st.set_page_config(page_title="台幣匯率轉換", layout="wide")
    st.title("台幣匯率轉換工具")
    
    # 手動更新按鈕
    if st.button("手動更新匯率資料"):
        st.cache_data.clear()
    
    # 取得匯率資料
    data = fetch_rates()
    rates = get_valid_rates(data)
    currency_options = [row["幣別"] for row in rates]
    
    col1, col2 = st.columns(2)
    with col1:
        st.header("台幣轉換為其他貨幣")
        amount = st.number_input("請輸入台幣金額", min_value=0.0, value=1000.0)
        currency = st.selectbox("選擇幣別", currency_options)
        rate_row = next((row for row in rates if row["幣別"] == currency), None)
        if rate_row and rate_row["本行即期賣出"] != "暫停交易":
            try:
                rate = float(rate_row["本行即期賣出"])
                result = amount / rate
                st.success(f"{amount:.2f} 台幣 ≈ {result:.2f} {currency}")
            except Exception:
                st.warning("匯率資料異常，無法計算。")
        else:
            st.info("此幣別暫停交易，無法換算。")
    with col2:
        st.header("匯率表格")
        st.dataframe(rates, use_container_width=True)
        st.caption("每10分鐘自動更新一次。欄位空值顯示為『暫停交易』。")

if __name__ == "__main__":
    main()
