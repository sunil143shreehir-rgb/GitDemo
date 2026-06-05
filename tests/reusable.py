import re
from playwright.sync_api import sync_playwright
import playwright
playwright = sync_playwright().start()
firefox = playwright.firefox
def call_to_ffbrowser():
    browser = firefox.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(5000) 
    print(page.title())
    def test_google_title():
        return re.match(r"Google", page.title()) 
    assert test_google_title() is not None, "Title does not match 'Google'"
    browser.close()
cromium = playwright.chromium
def call_to_chromium():
    browser = cromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(5000) 
    print(page.title())
    def test_google_title():
        return re.match(r"Google", page.title()) 
    assert test_google_title() is not None, "Title does not match 'Google'"
    browser.close()
mecrosoft_edge = playwright.chromium.launch(channel="msedge", headless=False)
def call_to_microsoft_edge():
    page = mecrosoft_edge.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(5000) 
    print(page.title())
    def test_google_title():
        return re.match(r"Google", page.title()) 
    assert test_google_title() is not None, "Title does not match 'Google'"
    mecrosoft_edge.close()  

