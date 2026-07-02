import re
from playwright.sync_api import sync_playwright
import playwright
import requests
playwright = sync_playwright().start()

firefox = playwright.firefox
def call_to_ffbrowser():
    browser = firefox.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(5000) 
    print(page.title())
    def test_google_title():
        return re.match(r"Google", page.title()) 
    assert test_google_title() is not None, "Title does not match 'Google'"
    return playwright, browser, page,context

cromium = playwright.chromium
def call_to_chromium():
    browser = cromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(5000) 
    print(page.title())
    def test_google_title():
        return re.match(r"Google", page.title()) 
    assert test_google_title() is not None, "Title does not match 'Google'"
    return playwright, browser, page,context

mecrosoft_edge = playwright.chromium.launch(channel="msedge", headless=False)
def call_to_microsoft_edge():
    browser = cromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    page = mecrosoft_edge.new_page()
    page.goto("https://www.google.com")
    page.wait_for_timeout(5000) 
    print(page.title())
    def test_google_title():
        return re.match(r"Google", page.title()) 
    assert test_google_title() is not None, "Title does not match 'Google'" 
    return playwright, browser, page,context

API_KEY = "0fb70df3b19231ce75c8e59f4c158a00"
#city = "Mumbai"
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"  #calling the API 
url2 = f"https://indian-railway-irctc.p.rapidapi.com/api/trains-search/v1/train"
response = requests.get(url)