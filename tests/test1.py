import re
from playwright.sync_api import sync_playwright
import playwright
import reusable
reusable.call_to_ffbrowser();
print("Firefox test completed.")
reusable.call_to_microsoft_edge();
print("Microsoft Edge test completed.")