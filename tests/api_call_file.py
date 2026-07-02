import requests 
from datetime import datetime, UTC, time, timedelta
import zoneinfo
import time


API_KEY = "0fb70df3b19231ce75c8e59f4c158a00"
#city = "Mumbai"
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"  #calling the API 

response = requests.get(url)
print("the response code is :" + str(response.status_code))

if response.status_code == 200:
    data = response.json()
else:
    print("Error:", data.get("message", "Something went wrong"))

data = response.json()
print("Printing the original data:", data)

# Extract useful info
temperature = data["main"]["temp"]
weather = data["weather"][0]["description"]
humidity = data["main"]["humidity"]
country = data["sys"]["country"]
timestamp = data["dt"]
timezone_offset = data["timezone"]

dt1 = datetime.fromtimestamp(time.time())
utc_time = datetime.fromtimestamp(timestamp, UTC)
local_time = (utc_time + timedelta(seconds=timezone_offset)).replace(tzinfo=None)
ist_time = datetime.fromtimestamp(timestamp, UTC).astimezone(zoneinfo.ZoneInfo("Asia/Kolkata"))

print("current time is :", dt1.strftime("%Y-%m-%d %H:%M:%S"))
print("UTC Date & Time:", utc_time)
print("Local Date & Time:", local_time)
print("IST Time:", ist_time)

# Convert to readable date
#date_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
#print("This is printing your Local city date & time:", date_time)
#print(f"Current Time: {dt1.strftime('%Y-%m-%d %H:%M:%S')}")

print(f"City: {city}")
print(f"Temperature: {temperature}°C")
print(f"Weather: {weather}")
print(f"Humidity: {humidity}%")  #here printing those values which are stored in variable in above steps
print(f"Country: {country}")

print(f"Feels like: {data['main']['feels_like']}°C") # here i am priniting values directly from jason data without storing in variable
print(f"Wind speed is: {data['wind']['speed']} m/s") 
