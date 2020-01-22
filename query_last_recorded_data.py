import sqlite3
conn = sqlite3.connect('sensor_data.db')
curs = conn.cursor()

print('\nLast data logged on database')
for row in curs.execute("""SELECT * FROM SENSOR_DATA
                           ORDER BY timestamp DESC
                           LIMIT 1"""):
    print(row)
