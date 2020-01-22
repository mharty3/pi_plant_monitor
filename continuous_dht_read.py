import time
import sqlite3
import Adafruit_DHT
import json
from pathlib import Path

# get the path to the database from the config file
# https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file
with open(Path('./config.json', 'r')) as f:
    config = json.load(f)
db_path = Path(config['db_path'])

sample_freq = 2 # time in seconds

# get the data from the sensor
def get_dht_data():
    DHT11_sensor = Adafruit_DHT.DHT11
    DHT_pin = 4
    hum, temp = Adafruit_DHT.read_retry(DHT11_sensor, DHT_pin)

    if hum is not None and temp is not None:
        hum = round(hum)
        temp = round(temp, 1)
        log_data(temp, hum)


# write the data to the database
def log_data(temp, hum):
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    curs.execute("INSERT INTO SENSOR_DATA values(datetime('now'), (?), (?))", (temp, hum))
    conn.commit()
    conn.close()

# display database data
def display_data():
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM SENSOR_DATA"):
        print(row)
    conn.close()

if __name__ == '__main__':
    for i in range(3):
        get_dht_data()
        time.sleep(sample_freq)
    display_data()

