import requests


API_KEY = "9fa1c30f950bd71a3c585a54a0da8bc8delhi" 


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


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
