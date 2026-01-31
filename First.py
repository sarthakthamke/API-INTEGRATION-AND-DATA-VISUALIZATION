import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

def fetch_weather_data(latitude, longitude):
    """
    Fetches hourly temperature data from the Open-Meteo API (free, no API key required).
    """
    # API endpoint URL
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Parameters for the API request
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "forecast_days": 5  # 5 days forecast
    }
    
    try:
        # Send a GET request to the API
        response = requests.get(url, params=params)
        print(f"Response status: {response.status_code}")
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            print("Data fetched successfully")
            return data
        else:
            print(f"Error fetching data: Status code {response.status_code}")
            print(response.text)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
        return None

def visualize_temperature_matplotlib(data):
    """
    Visualizes the fetched temperature data using Matplotlib.
    """
    if not data or "hourly" not in data:
        print("Invalid data format for visualization.")
        return

    # Extract timestamps and temperatures
    timestamps = [datetime.fromisoformat(t) for t in data["hourly"]["time"]]
    temperatures = data["hourly"]["temperature_2m"]

    # Plotting using Matplotlib
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='b', label='Temperature')
    
    # Customize the plot
    plt.title("5-Day Hourly Temperature Forecast")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
    # Save and display the plot
    plt.savefig('temperature_plot_matplotlib.png')
    plt.show()

def visualize_temperature_seaborn(data):
    """
    Visualizes the fetched temperature data using Seaborn.
    """
    if not data or "hourly" not in data:
        print("Invalid data format for visualization.")
        return

    # Extract timestamps and temperatures
    timestamps = [datetime.fromisoformat(t) for t in data["hourly"]["time"]]
    temperatures = data["hourly"]["temperature_2m"]

    # Plotting using Seaborn
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=timestamps, y=temperatures, marker='o', color='b', label='Temperature')
    
    # Customize the plot
    plt.title("5-Day Hourly Temperature Forecast")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
    # Save and display the plot
    plt.savefig('temperature_plot_seaborn.png')
    plt.show()

# Main execution
if __name__ == "__main__":
    # Coordinates for Berlin, Germany (you can change to any location)
    LATITUDE = 52.52
    LONGITUDE = 13.41
    
    weather_data = fetch_weather_data(LATITUDE, LONGITUDE)
    
    if weather_data:
        # Using Matplotlib for visualization
        visualize_temperature_matplotlib(weather_data)
    else:
        print("Could not retrieve weather data.")