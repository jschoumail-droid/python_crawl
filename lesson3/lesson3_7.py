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