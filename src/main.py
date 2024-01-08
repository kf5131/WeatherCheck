import os
import requests

from dotenv import load_dotenv


def get_weather(api_key, city):
    '''Returns weather data for the given city, or None if the city is not found.'''
    #api_key = os.getenv("API_KEY")
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  # Adjust units as needed
    try:
        response = requests.get(base_url, params=params, timeout=5)  # Added timeout argument
        data = response.json()
    except requests.exceptions.RequestException as e:  # Specify the exception type
        if e.response:
            print(e.response.status_code)
        return None

    if response.status_code == 200:
        return data
    else:
        return None
    
    
def main():
    '''Main function.'''

    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("OPENWEATHERMAP_API_KEY") # Get API key from environment variable
    
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)

    if weather_data:
        # Extract and display relevant information from the 'weather_data' dictionary
        print(f"Weather in {city}: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
    else:
        print("Error fetching weather data. Please check your city name and API key.")
        
    
if __name__ == "__main__":
    main()
