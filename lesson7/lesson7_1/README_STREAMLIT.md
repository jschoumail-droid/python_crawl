# lesson7_1 — 台幣匯率轉換（Streamlit）

此專案使用 `crawl4ai` 抓取台灣銀行牌告匯率，並以 `streamlit` 提供兩欄 UI：左側為台幣轉換計算器，右側為匯率表格。

快速開始

1. 建議建立虛擬環境：

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

2. 安裝 Playwright 瀏覽器驅動（必要）：

```powershell
python -m playwright install
```

3. 啟動 Streamlit 應用：

```powershell
streamlit run main.py
```

注意事項

- 若在 Windows 環境遇到 Playwright 或 asyncio 的子程序相容性問題，請確保使用標準 CPython 並可嘗試在程式啟動處加上：

```python
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
```

- 若 `crawl4ai` 需要 API key 或環境設定，請依 `crawl4ai` 文件設定環境變數。

- 預設使用 `st.cache_data(ttl=600)` 每 10 分鐘更新快取；可使用介面上的「🔄 手動更新」強制刷新。
