import sys
import subprocess
import csv
import geoip2
import geoip2.database

from subprocess import check_output
destination=input("Enter webpage you wish to traceroute: ")
tmp_out = check_output(["traceroute",destination])
out = str(tmp_out, 'utf-8')
print(out)

fileToRead = "/home/kaisa/Documents/Python/Project/test.csv" 
fileToWrite = "/home/kaisa/Documents/Python/Project/test2.csv" 

def stringToCsv(data, csvFileToWrite):
    index=(data.find('(')) + 1
    csv_write = open(csvFileToWrite, "w")
    
    while index < data.rfind(')'):
        i = data.find('(', index)
        j = data.find(')', index)
        temp= data[i+1:j]
        index = j+1
        if temp != '':
            row = temp+'\n'
            csv_write.write(row)
        
    return csv_write;
    
stringToCsv(out,fileToRead)

geo_data = '/home/kaisa/Documents/Python/GeoLite2/GeoLite2-City.mmdb'


def latLongToCsv(dbase, csvFileToRead, csvFileToWrite):
    reader = geoip2.database.Reader(dbase)
    csv_read = open(csvFileToRead, 'r')
    csv_write = open(csvFileToWrite, 'w')
    read_csv = csv.reader(csv_read)
    for row in read_csv:
        str_row =row[0]
        try:
            response = reader.city(str_row)
        except:
            print('oh no')
            pass
        else:
            latitude = response.location.latitude
            longitude = response.location.longitude
            print(latitude, longitude)
            new_row =  "{0:f}, {1:f}\n".format(latitude, longitude)
            csv_write.write(new_row)
        
    return csv_write;
    

        
latLongToCsv(geo_data,fileToRead, fileToWrite)

