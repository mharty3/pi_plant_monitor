from flask import Flask, render_template, request
app = Flask(__name__)

import sqlite3

# Retrieve data from database
def get_data():
    conn = sqlite3.connect('../sensor_data.db')
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
