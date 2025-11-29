from playwright.sync_api import sync_playwright
import os 
import os

def get_html_path()->str:
    path=os.path.dirname(os.path.abspath(__file__))
    html_path=os.path.join(path,"waiting_demo.html")
    return f'file://{html_path}'

def demo_1_delayed_element(page):
    # 等待載入指示器出現
    page.wait_for_selector("#loading-1", state="visible")
    print("載入指示器已出現")
    # 等待載入指示器消失
    page.wait_for_selector("#loading-1", state="hidden")
    print("載入指示器已消失")
    page.wait_for_selector("div#delayed-result.result.show", state="visible")
    # 取得內容
    content = page.locator("#delayed-content").text_content()
    print(f"延遲加載的內容: {content}")

def demo_2_dynamic_content(page):
    page.click("#load-data")  # 點擊按鈕觸發異步操作

    #page.wait_for_selector("#dynamic-content", state="visible")
    page.wait_for_function("document.querySelectorAll('#dynamic-content > .item').length >= 3")
    items = page.locator("#dynamic-content > .item").all()
    for item in items:
        print(f"動態加載的項目: {item.text_content()}")


def main():
    html_path=get_html_path()
    print(html_path)

    with sync_playwright() as p:
        # Launch the browser
        browser=p.chromium.launch(headless=False,slow_mo=500)
        # Create a new page
        page=browser.new_page()
        # Navigate to the HTML file
        page.goto(html_path)
        # Wait for the page to load
        page.wait_for_load_state("networkidle")

        #page.click("#trigger-delayed")
        delay_button=page.locator("#trigger-delayed")
        delay_button.click()

        demo_1_delayed_element(page)
        demo_2_dynamic_content(page)


        # Wait for 3 seconds
        page.wait_for_timeout(3000)

        browser.close()

    print(html_path)

if __name__=="__main__":
    main()