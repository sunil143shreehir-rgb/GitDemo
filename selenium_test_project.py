from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

# Open Gmail
driver.get("https://mail.google.com")

time.sleep(3)

# Enter email
email_input = driver.find_element(By.ID, "identifierId")
email_input.send_keys("your_email@gmail.com")
email_input.send_keys(Keys.ENTER)

time.sleep(3)

# Enter password (NOT recommended to hardcode)
password_input = driver.find_element(By.NAME, "Passwd")
password_input.send_keys("your_password")  # avoid this in real use
password_input.send_keys(Keys.ENTER)