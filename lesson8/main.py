import asyncio
import json
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkfont
from threading import Thread
from datetime import datetime
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup

from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

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


def _run_async_fn(fn, *args, **kwargs):
    try:
        return asyncio.run(fn(*args, **kwargs))
    except Exception:
        try:
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
        except Exception:
            pass
        return asyncio.run(fn(*args, **kwargs))


def fetch_exchange_rates() -> List[Dict[str, str]]:
    # Try async Playwright-based fetch first
    try:
        data = _run_async_fn(_fetch_async)
    except Exception:
        # fallback to requests + bs4
        url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW'
        resp = requests.get(url, timeout=10)
        resp.encoding = resp.apparent_encoding
        soup = BeautifulSoup(resp.text, 'html.parser')
        table = soup.select_one("table[title='牌告匯率']")
        rows = []
        if table:
            for tr in table.select('tr'):
                cur = tr.select_one("td[data-table='幣別'] div.print_show")
                buy = tr.select_one("td[data-table='本行即期買入']")
                sell = tr.select_one("td[data-table='本行即期賣出']")
                if cur is None:
                    continue
                rows.append({
                    '幣別': cur.get_text(strip=True),
                    '本行即期買入': buy.get_text(strip=True) if buy else '',
                    '本行即期賣出': sell.get_text(strip=True) if sell else ''
                })
        data = rows

    # normalize
    cleaned: List[Dict[str, str]] = []
    for item in data:
        buy = (item.get('本行即期買入') or '').strip()
        sell = (item.get('本行即期賣出') or '').strip()
        if buy == '' and sell == '':
            continue
        cleaned.append({
            '幣別': item.get('幣別', '').strip(),
            '本行即期買入': buy if buy else '暫停交易',
            '本行即期賣出': sell if sell else '暫停交易'
        })
    return cleaned


class ExchangeRateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('台灣銀行匯率查詢')
        self.geometry('1000x600')
        self.exchange_data: List[Dict[str, str]] = []
        self.last_update: Optional[datetime] = None
        self._setup_ui()
        self._load_initial_data()

    def _setup_ui(self):
        # Fonts and styles
        default_font = tkfont.nametofont("TkDefaultFont")
        font_label = tkfont.Font(family=default_font.actual('family'), size=16)
        font_button = tkfont.Font(family=default_font.actual('family'), size=16, weight='bold')
        font_tree = tkfont.Font(family=default_font.actual('family'), size=14)
        font_heading = tkfont.Font(family=default_font.actual('family'), size=16, weight='bold')
        font_result = tkfont.Font(family=default_font.actual('family'), size=14)

        style = ttk.Style()
        # Use default theme's look but increase row height and fonts
        style.configure('Treeview', rowheight=34, font=font_tree)
        style.configure('Treeview.Heading', font=font_heading)

        top = ttk.Frame(self)
        top.pack(fill='x', padx=10, pady=10)
        self.update_btn = ttk.Button(top, text='🔄 更新匯率', command=self._on_update_clicked)
        self.update_btn.pack(side='left')
        self.update_btn.configure(style='TButton')
        self.update_btn.configure(font=font_button)
        self.time_label = ttk.Label(top, text='最後更新：-')
        self.time_label.pack(side='left', padx=16)
        self.time_label.configure(font=font_label)

        main = ttk.Frame(self)
        main.pack(fill='both', expand=True, padx=10, pady=10)

        left = ttk.Frame(main)
        left.pack(side='left', fill='both', expand=True)
        right = ttk.Frame(main)
        right.pack(side='right', fill='both', expand=False)

        # Treeview
        cols = ('幣別', '本行即期買入', '本行即期賣出')
        self.tree = ttk.Treeview(left, columns=cols, show='headings', height=20)
        for c in cols:
            self.tree.heading(c, text=c)
        # wider columns for readability
        self.tree.column('幣別', width=320, anchor='w')
        self.tree.column('本行即期買入', width=160, anchor='center')
        self.tree.column('本行即期賣出', width=160, anchor='center')
        vsb = ttk.Scrollbar(left, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        self.tree.pack(side='left', fill='both', expand=True)
        vsb.pack(side='left', fill='y')

        # Right: conversion (use grid inside right frame to make result_text expandable)
        right.grid_rowconfigure(6, weight=1)
        right.grid_columnconfigure(0, weight=1)

        lbl_amt = ttk.Label(right, text='台幣金額')
        lbl_amt.grid(row=0, column=0, sticky='w', pady=(8,4), padx=8)
        lbl_amt.configure(font=font_label)

        self.twd_var = tk.StringVar(value='1000')
        self.twd_entry = ttk.Entry(right, textvariable=self.twd_var, font=font_label)
        self.twd_entry.grid(row=1, column=0, sticky='ew', padx=8)

        lbl_cur = ttk.Label(right, text='目標貨幣')
        lbl_cur.grid(row=2, column=0, sticky='w', pady=(12,4), padx=8)
        lbl_cur.configure(font=font_label)

        self.currency_cb = ttk.Combobox(right, values=[], state='readonly', font=font_label)
        self.currency_cb.grid(row=3, column=0, sticky='ew', padx=8)

        calc_btn = ttk.Button(right, text='計算', command=self._calculate)
        calc_btn.grid(row=4, column=0, pady=12, padx=8)
        calc_btn.configure(font=font_button)

        # Make result_text expand with window
        self.result_text = tk.Text(right, height=8, wrap='word', font=font_result)
        self.result_text.grid(row=6, column=0, sticky='nsew', padx=8, pady=8)
        # add a vertical scrollbar for result_text
        res_vsb = ttk.Scrollbar(right, orient='vertical', command=self.result_text.yview)
        self.result_text.configure(yscrollcommand=res_vsb.set)
        res_vsb.grid(row=6, column=1, sticky='ns')

    def _on_update_clicked(self):
        self.update_btn.config(state='disabled')
        thread = Thread(target=self._fetch_data_thread, daemon=True)
        thread.start()

    def _load_initial_data(self):
        self._on_update_clicked()

    def _fetch_data_thread(self):
        try:
            data = fetch_exchange_rates()
            self.after(0, lambda: self._update_ui_with_data(data))
        except Exception as e:
            self.after(0, lambda: messagebox.showerror('錯誤', f'抓取失敗: {e}'))
        finally:
            self.after(0, lambda: self.update_btn.config(state='normal'))

    def _update_ui_with_data(self, data: List[Dict[str, str]]):
        self.exchange_data = data
        self.last_update = datetime.now()
        self.time_label.config(text=f'最後更新：{self.last_update.strftime("%Y-%m-%d %H:%M:%S")}')
        for i in self.tree.get_children():
            self.tree.delete(i)
        for row in data:
            self.tree.insert('', 'end', values=(row['幣別'], row['本行即期買入'], row['本行即期賣出']))
        # update combobox (filter tradable)
        vals = [r['幣別'] for r in data if r['本行即期賣出'] != '暫停交易']
        self.currency_cb['values'] = vals
        if vals:
            self.currency_cb.current(0)

    def _calculate(self):
        try:
            twd = float(self.twd_var.get())
        except Exception:
            messagebox.showerror('錯誤', '請輸入有效數字')
            return
        cur = self.currency_cb.get()
        if not cur:
            messagebox.showwarning('警告', '請選擇貨幣')
            return
        row = next((r for r in self.exchange_data if r['幣別'] == cur), None)
        if not row:
            messagebox.showerror('錯誤', '找不到匯率資料')
            return
        sell = row['本行即期賣出']
        if sell == '暫停交易':
            messagebox.showwarning('警告', '此幣別暫停交易')
            return
        try:
            rate = float(sell)
            foreign = twd / rate
            self.result_text.delete('1.0', 'end')
            self.result_text.insert('end', f"{twd:,.2f} TWD = {foreign:,.4f} {cur}\n使用匯率: {rate}")
        except Exception:
            messagebox.showerror('錯誤', '匯率格式錯誤')


def main():
    app = ExchangeRateApp()
    app.mainloop()


if __name__ == '__main__':
    main()
