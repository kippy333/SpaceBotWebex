import requests
import time

current_timestamp = int(time.time())
print(current_timestamp)

URL = "https://api.wheretheiss.at/v1/"

def getSatellites(url):
    response = requests.get(url + "satellites")
    satellites = response.json()
    for sat in satellites:
        print(sat['name'], sat['id'])

getSatellites(URL)

def getPosition(url, timestamp):
    response = requests.get(url + "satellites/25544/positions?timestamps=" + str(timestamp))
    positions = response.json()
    for pos in positions:
        print(pos['longitude'], pos['latitude'])

getPosition(URL, current_timestamp)