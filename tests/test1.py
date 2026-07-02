import re
#import requests
from playwright.sync_api import sync_playwright
import playwright
import reusable
playwright, browser, page, context = reusable.call_to_microsoft_edge(); 
page.goto("https://www.indianrail.gov.in/")
page.wait_for_timeout(5000)
print(page.title())
if page.title() == "Welcome to Indian Railway Passenger Reservation Enquiry":
    print("Test passed: Title matches - 'indian railways inquiry site opened successfully'")
else:
    print("Test failed: Title does not match - 'indian railways inquiry site does not opened successfully'")  
##print("Microsoft Edge test completed.")

reusable.call_to_api()
print("API call completed successfully.")


"""
payload = {
    "from": "BBS",
    "to": "NDLS",
    "date": "2026-07-02"
}

headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
browser.close()
"""