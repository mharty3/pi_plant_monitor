# pi_plant_monitor

This is a project to experiment with collecting, storing, and serving sensor data with a raspberry pi. It is inspired by [this tutorial](https://www.instructables.com/id/From-Data-to-Graph-a-Web-Jorney-With-Flask-and-SQL/).

## Project set up
A few things need to be done to start the project.

### Initialize database
Install sqlite3: `sudo apt-get install sqlite3`

```
>>>sqlite3 sensorsData.db

sqlite> BEGIN;
sqlite> CREATE TABLE SENSOR_DATA (timestamp DATETIME,  temp NUMERIC, hum NUMERIC);
sqlite> COMMIT;
sqlite> .quit
```

### Write the database path to the config file
Write the following to **config.json** and store it in the pi_plant_monitor directory: `{"db_path": "/full/path/to/database.db"}`
The python files will read the config file to know where to find the database.

### Set up cron to record measurements at particular intervals
* * * * * cd /home/pi/pi_plant_monitor/ && /home/pi/pi_plant_monitor/pi_plant_monitor_venv/bin/python3 ~/pi_plant_monitor/continuous_dht_read.py >> /home/pi/pi_plant_monitor/cronlog.log 2>&1
