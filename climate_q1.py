import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

connection = sqlite3.connect('climate.db')
cursor = connection.cursor()
cursor.execute("SELECT * FROM ClimateData")
result = cursor.fetchall()

for row in result:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])

cursor.close()
connection.close()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_1.png")
