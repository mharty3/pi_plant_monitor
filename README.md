# pi_plant_monitor

This is a project to experiment with collecting, storing, and serving sensor data with a raspberry pi. It is inspired by [this tutorial](https://www.instructables.com/id/From-Data-to-Graph-a-Web-Jorney-With-Flask-and-SQL/).

## Project set up
A few things need to be done to start the project.

### Initialize database
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
