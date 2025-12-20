
import asyncio,json
from crawl4ai import AsyncWebCrawler,CrawlerRunConfig,CacheMode
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def main():
    html = """
<div class="item">
    <h2>項目1</h2>
    <a href="https://example.com/item1">連結1</a>
</div>"""
import asyncio
from datetime import datetime
import streamlit as st
import pandas as pd
from crawler import fetch_exchange_rates_raw


@st.cache_data(ttl=600)
def fetch_exchange_rates():
    """Fetch and return cleaned DataFrame (cached for 10 minutes)."""
    return fetch_exchange_rates_raw()


def main():
    st.set_page_config(page_title="台幣匯率轉換", page_icon="💱", layout="wide")
    st.title("💱 台幣匯率轉換系統")

    # 手動更新按鈕
    cols = st.columns([6, 1])
    with cols[1]:
        if st.button("🔄 手動更新", use_container_width=True):
            st.cache_data.clear()
            st.experimental_rerun()

    st.info(f"📅 最後更新時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    try:
        df = fetch_exchange_rates()
        if df is None or df.empty:
            st.error("❌ 無法取得匯率資料")
            return

        # 過濾可交易的貨幣
        tradable_df = df[~((df['本行即期買入'] == '暫停交易') & (df['本行即期賣出'] == '暫停交易'))].copy()

        if tradable_df.empty:
            st.warning("⚠️ 目前沒有可交易的貨幣")
            return

        col1, col2 = st.columns([1, 1])

        with col1:
            st.subheader("💰 台幣轉換計算器")
            twd_amount = st.number_input("輸入台幣金額 (TWD)", min_value=0.0, value=1000.0, step=100.0, format="%.2f")
            currency_list = tradable_df['幣別'].tolist()
            selected_currency = st.selectbox("選擇目標貨幣", currency_list)

            if selected_currency:
                row = tradable_df[tradable_df['幣別'] == selected_currency].iloc[0]
                sell_rate = row['本行即期賣出']
                if sell_rate != '暫停交易':
                    try:
                        sell_rate_float = float(sell_rate)
                        foreign_amount = twd_amount / sell_rate_float
                        st.success(f"{twd_amount:,.2f} TWD = {foreign_amount:,.4f} {selected_currency}")
                        st.caption(f"使用匯率：{sell_rate_float:.4f} (本行賣出)")
                    except Exception:
                        st.error("❌ 匯率資料格式錯誤，無法計算")
                else:
                    st.warning("⚠️ 此貨幣暫停交易")

        with col2:
            st.subheader("📊 台灣銀行牌告匯率")
            st.dataframe(tradable_df, use_container_width=True, hide_index=True)
            st.caption("每10分鐘自動更新一次（使用快取 TTL）。欄位空值顯示為『暫停交易』。")

    except Exception as e:
        st.error(f"❌ 發生錯誤：{str(e)}")


if __name__ == "__main__":
    main()