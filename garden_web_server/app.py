from flask import Flask, render_template, request
import sqlite3
from path import Path
import json

# get the path to the database from the config file
# https://stackoverflow.com/questions/19078170/python-how-would-you-save-a-simple-settings-config-file
with open(Path('../config.json', 'r')) as f:
    config = json.load(f)
db_path = Path(config['db_path'])

app = Flask(__name__)
# Retrieve data from database

def get_data():
    conn = sqlite3.connect(db_path)
    curs = conn.cursor()

    for row in curs.execute("SELECT * FROM SENSOR_DATA ORDER BY timestamp DESC LIMIT 1"):
        time = str(row[0])
        temp = row[1]
        hum = row[2]
    conn.close()
    return time, temp, hum

# main route
@app.route("/")
def index():
    time, temp, hum = get_data()
    template_data = {
            "time": time,
            "temp": temp,
            "hum": hum,
            }
    return render_template("index.html", **template_data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
