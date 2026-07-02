from http.client import responses
import json
import re
from urllib import response 
from playwright.sync_api import sync_playwright
import playwright
import requests
import reusable
import pandas as pd
from tabulate import tabulate

playwright, browser, page, context = reusable.call_to_microsoft_edge(); 
page.goto("https://www.indianrail.gov.in/")
page.wait_for_timeout(5000)
print(page.title())
if page.title() == "Welcome to Indian Railway Passenger Reservation Enquiry":
    print("Test passed: Title matches - 'indian railways inquiry site opened successfully'")
else:
    print("Test failed: Title does not match - 'indian railways inquiry site does not opened successfully'")  
##print("Microsoft Edge test completed.")

def call_to_railway_api():
   API_KEY = "rg_af9dfc25d1ca41ddbe6a638b2361899f"
   date = input ("enter search date: ")
   from_city = input ("enter source city station code : ").strip().upper()
   to_city = input ("enter destination city station code : ").strip().upper()
   headers = {"Authorization": f"Bearer {API_KEY}"}

  # url1 = f"https://api.railradar.in/v1/trains/between/{from_city}/{to_city}?date={date}"
  #response1 = requests.get(url1, headers=headers)
   response1 = requests.get(f"https://api.railradar.in/v1/trains/12919/live", headers=headers)
   response2 = requests.get(f"https://api.railradar.in/v1/trains/between/{from_city}/{to_city}?date={date}", headers=headers)
   return response1, response2
Train_live_status, Trains_between = call_to_railway_api()
#print(Train_live_status.status_code) 
#print(Train_live_status.json()) # gives you the live status of the train
#print(Trains_between.status_code) 
#print(Trains_between.json()) # gives you the trains between source and destination
#print(Trains_between.text) # gives you the trains between source and destination in text format

#btrains_between=Trains_between.json()["data"]
#print(btrains_between)
response = Trains_between.json()
#print(response)
trains = response["data"]["trains"]
df = pd.json_normalize(trains)   #this will create the data in a table format
#df = pd.json_normalize(Trains_between.json()["data"]["trains"])   #this will create the data in a table format
print(df)




table = []
btrains_between=Trains_between.json()["data"]
#print(btrains_between)
for train in btrains_between["trains"]: 
    table.append([
        train["train"]["number"],
        train["train"]["name"],
        train["train"]["type"],
        train["from"]["departure"],
        train["to"]["arrival"],
        train["distance"],
        train["duration"],
        train["totalHaltsBetween"]
    ])

print(tabulate(
    table,
    headers=[
        "Train No",
        "Train Name",
        "Train Type",
        "Departure Time",
        "Arrival Time",
        "Distance",
        "Duration",
        "Total Halts"
    ],
    tablefmt="grid"
))

browser.close()