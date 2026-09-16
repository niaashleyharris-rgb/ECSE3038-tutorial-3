from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

#write a function called average_temp(devices) — return the average temperature
def average_temp(devices):
    total = sum(device['temp'] for device in devices)
    return total / len(devices)

print(f"Average Temperature: {average_temp(readings):.2f}°C")

#write a function called hottest(devices) — return the whole dictionary of the hottest device
def hottest(devices):
    return max(devices, key=lambda device: device['temp'])

print(f"Hottest Device: {hottest(readings)['name']}, Temperature: {hottest(readings)['temp']}") 

#write a get request with path GET /devices that returns the list of devices
@app.get("/devices")
def get_devices():
    return readings

