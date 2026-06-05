import re
from playwright.sync_api import sync_playwright
import playwright
import reusable
playwright, browser, page, context = reusable.call_to_microsoft_edge(); 
page.goto("https://www.indianrail.gov.in/")
page.wait_for_timeout(5000)
print(page.title())
if page.title() == "indianrailways.com - Passenger Enquiry":
    print("Test passed: Title matches 'indianrailways.com - Passenger Enquiry'")
else:
    print("Test failed: Title does not match 'indianrailways.com - Passenger Enquiry'")  
print("Microsoft Edge test completed.")
browser.close()