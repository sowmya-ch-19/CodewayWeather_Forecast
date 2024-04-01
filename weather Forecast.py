import requests
city_or_zip = input("Enter a city name or a ZIP code: ")
api_key = 'YOUR_API_KEY'
url = f"http://api.openweathermap.org/data/2.5/weather?q={city_or_zip}&appid={api_key}&units=metric"
response = requests.get(url)
weather_data = response.json()
if weather_data.get('cod') == 200:  # Status code 200 means success
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    description = weather_data['weather'][0]['description']
else:
    print("Error retrieving weather data. Please check your input.")
    exit()
print(f"Weather in {city_or_zip}:")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed} m/s")
print(f"Description: {description.capitalize()}")
