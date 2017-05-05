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

c_file = "/home/kaisa/Documents/Python/test.csv" 

def stringToCsv(data, url):
    index=(data.find('(')) + 1
    download_dir = url
    csv = open(download_dir, "w")
    
    while index < data.rfind(')'):
        i = data.find('(', index)
        j = data.find(')', index)
        temp= data[i+1:j]
        index = j+1
        if temp != '':
            row = temp+'\n'
            csv.write(row)
        
    return csv;
    
stringToCsv(out,c_file)

geo_data = '/home/kaisa/Documents/Python/GeoLite2/GeoLite2-City.mmdb'


