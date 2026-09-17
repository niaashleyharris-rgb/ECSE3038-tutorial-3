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

#write a request with path GET /devices/hottest that returns the device with the highest temperature
@app.get("/devices/hottest")
def get_hottest_device():
    return hottest(readings)

#write a request with path GET /devices/online that returns only the devices whose online is true
@app.get("/devices/online")
def get_online_devices():
    return [device for device in readings if device['online']]

#write a request with path GET /devices/{name} that returns One device, or a 404
@app.get("/devices/{name}")
async def get_reading_by_name(name: str): #the str is forcing python to expect a string for the name parameter
    for reading in readings:
        if reading["name"] == name:
            return reading
            #we are raising an excpetion if we expect the user insert something off
    raise HTTPException(status_code=404, detail="Reading not found")

#write a request with path GET /stats that returns the average temperature of every device
@app.get("/stats")
def get_average_temperature():
    return {"average_temperature": average_temp(readings)}


#write a request with path POST /devices that returns The new device, with status 201 
@app.post("/devices", status_code=201)
async def post_reading(reading: dict):
    readings.append(reading)
    return reading
    #return code that ensures a 201 is returned to the client upon success 

#write a request with path Stretch. GET /rooms/{room}/devices that returns Every device in that room, in full, or a 404
@app.get("/rooms/{room}/devices")
async def get_devices_in_room(room:str):
    room_devices = [device for device in readings if device['room'] == room]
    if not room_devices:
        raise HTTPException(status_code=404, detail="No devices found in this room")
    return room_devices