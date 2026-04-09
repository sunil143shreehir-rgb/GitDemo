import requests

API_KEY = "0fb70df3b19231ce75c8e59f4c158a00"
#city = "Mumbai"
city = input("Enter city name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
print("the response code is :" + str(response.status_code))

if response.status_code == 200:
    data = response.json()
else:
    print("Error:", data.get("message", "Something went wrong"))

data = response.json()
print(data)

# Extract useful info
temperature = data["main"]["temp"]
weather = data["weather"][0]["description"]
humidity = data["main"]["humidity"]

print(f"City: {city}")
print(f"Temperature: {temperature}°C")
print(f"Weather: {weather}")
print(f"Humidity: {humidity}%")