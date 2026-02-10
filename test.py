print("Script started")
import requests
print("Requests imported")
response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m&forecast_days=1")
print(f"Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    print("Data keys:", list(data.keys()))
    print("Hourly keys:", list(data["hourly"].keys()) if "hourly" in data else "No hourly")
    print("First 5 temps:", data["hourly"]["temperature_2m"][:5] if "hourly" in data and "temperature_2m" in data["hourly"] else "No temp data")
else:
    print("Response text:", response.text)
print("Script ended")