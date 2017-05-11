from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import csv
import sys


# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
plt.figure(figsize=(30,15))
my_map = Basemap()
my_map.drawcoastlines(color='grey')

my_map.fillcontinents(color='grey')
my_map.drawmapboundary(color='grey')

geo_csv = "/home/kaisa/Documents/Python/Project/test2.csv"

def pointsFromCsvFile(csvFileToRead):
    csv_read = open(csvFileToRead, "r")
    read_csv = csv.reader(csv_read) #is this necessary?
    temp_lat = 0.0
    temp_long = 0.0
    for row in read_csv: 
        if temp_lat == 0.0 and temp_long == 0.0:
            latitude = float(row[0])
            longitude = float(row[1])
            x,y = my_map(longitude, latitude)
            my_map.plot(x,y,'ro', markersize=4)
            temp_lat = latitude
            temp_long = longitude
        else:
            latitude = float(row[0])
            longitude = float(row[1])
            my_map.drawgreatcircle(temp_long, temp_lat, longitude,latitude)
            x,y = my_map(longitude, latitude)
            my_map.plot(x,y,'ro', markersize=4)
            temp_lat = latitude
            temp_long = longitude



pointsFromCsvFile(geo_csv)       

plt.show()

