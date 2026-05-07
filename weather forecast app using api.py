import requests

# Replace with your actual OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Take city name input
city = input("Enter city name: ")

# Parameters for API request
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    # Send GET request
    response = requests.get(BASE_URL, params=params)

    # Convert response to JSON
    data = response.json()

    # Check if request was successful
    if response.status_code == 200:
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print("\nWeather Report")
        print("City:", data["name"])
        print("Temperature:", temp, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", weather.title())

    else:
        print("Error:", data.get("message", "City not found!"))

except requests.exceptions.RequestException as e:
    print("Network error:", e)