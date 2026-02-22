import requests
import matplotlib.pyplot as plt

# OpenWeatherMap API key
api_key = "a10175ba1d9647b34f463967acb683fc"

# cities selected by me
my_cities = ["yavatmal", "Wardha", "nagpur"]

# empty lists to store weather values
temperature_list = []
pressure_list = []

# fetching data city by city
for place in my_cities:
    api_url = (
        "https://api.openweathermap.org/data/2.5/weather"
        "?q=" + place +
        "&appid=" + api_key +
        "&units=metric"
    )

    response = requests.get(api_url)
    weather_data = response.json()

    # extracting required data
    city_temperature = weather_data["main"]["temp"]
    city_pressure = weather_data["main"]["pressure"]

    temperature_list.append(city_temperature)
    pressure_list.append(city_pressure)

    print("City:", place)
    print("Temperature:", city_temperature, "°C")
    print("Pressure:", city_pressure, "hPa")
    print("-------------------")

# Temperature bar graph
plt.figure()
plt.bar(my_cities, temperature_list)
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Comparison of Cities")
plt.show()

# Pressure line graph
plt.figure()
plt.plot(my_cities, pressure_list)
plt.xlabel("City")
plt.ylabel("Pressure (hPa)")
plt.title("Atmospheric Pressure Analysis")
plt.show()