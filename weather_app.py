import requests

print("Weather App 🌦️")

city = input("Enter city name: ")

api_key = "2440c05181f949f2a58ee6422ebf665a"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

print(data)

if data["cod"] == 200:

    temperature = data["main"]["temp"]
    weather = data["weather"][0]["description"]
    humidity = data["main"]["humidity"]

    print("\nWeather Report 🌍")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Condition:", weather)
    print("Humidity:", humidity, "%")

else:
    print("City not found ❌")