from playwright.sync_api import sync_playwright
import time


URL = 'https://sfbay.craigslist.org/'

playwright = sync_playwright().start()

browser = playwright.firefox.launch(headless=False)

page = browser.new_page(
    java_script_enabled=True,
    viewport={"width": 1280, "height": 800}
)
page.goto(URL, wait_until='load')

time.sleep(10)
page.close()
browser.close()
playwright.stop()



# this code contain basic playwright navigation and page setip for web scraping

