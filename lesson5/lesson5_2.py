from playwright.sync_api import sync_playwright
import os

def get_html_path()->str:
    path=os.path.dirname(os.path.abspath(__file__))
    html_path=os.path.join(path,"waiting_demo.html")

    return f'file://{html_path}'

def get_news(page):
    lis = page.locator("ul#alltype-news.news-list > li").all()
    print(type(lis))
    print(f"共找到 {len(lis)} 筆最新消息")
    for item in lis:
        date = item.locator("div.news-date").text_content()
        title = item.locator("div.news-title").text_content()
        print(date)
        print(title)
        print("=" * 60)


def main():
    #html_path=get_html_path()
    #print(html_path)
    html_path = "https://www.thsrc.com.tw/"

    with sync_playwright() as p:
        # Launch the browser
        browser=p.chromium.launch(headless=False,slow_mo=500)
        # Create a new page
        page=browser.new_page()
        # Navigate to the HTML file
        page.goto(html_path)
        # Wait for the page to load
        page.wait_for_load_state("domcontentloaded")

        page.locator("button",has_text="我同意").click()  # 點擊按鈕觸發異步操作

        get_news(page)
        # Wait for 3 seconds
        page.wait_for_timeout(3000)

        browser.close()

    print(html_path)

if __name__=="__main__":
    main()