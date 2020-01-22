import Adafruit_DHT
DHT11_Sensor = Adafruit_DHT.DHT11
DHTpin = 4 

hum, temp = Adafruit_DHT.read_retry(DHT11_Sensor, DHTpin)
if hum is not None and temp is not None:
    print(f'Temp: {temp} degC | Humidity: {hum}%')
else:
    print('Failed to read. Try again.')
