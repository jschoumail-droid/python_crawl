from playwright.sync_api import sync_playwright, Playwright
from time import sleep

def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    #browser = chromium.launch() #不顯示網頁
    browser = chromium.launch(headless=False) #顯示網頁
    
    page = browser.new_page()
    page.goto("http://example.com")
    # other actions...
    # 取得標題
    print(page.title())
    
    sleep(5)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

'''
# 此例每有使用 with 語法，就必須手動管理啟動與關閉

from playwright.sync_api import sync_playwright

# 1. 呼叫函式取得管理器
manager = sync_playwright() 

# 2. 手動啟動（這就是 with 幫你做的事）
p = manager.start() 

# 3. 此時 p 是物件，可以操作
browser = p.chromium.launch(headless=False)

# 4. 結束後必須手動關閉
p.stop()
'''


'''
# Terminates this instance of Playwright in case
# it was created bypassing the Python context manager.
# This is useful in REPL applications.

from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="example.png")
browser.close()

playwright.stop()
'''
