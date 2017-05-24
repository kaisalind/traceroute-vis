import argparse
import geoip2.database
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
from subprocess import check_output


def ipToDict(data):
    my_dict={};
    index=(data.find('(')) + 1
    
    for d in data:
        while index < data.rfind(')'):
                i = data.find('(', index)
                j = data.find(')', index)
                temp= data[i+1:j]
                index = j+1
                if temp != '':
                    my_dict[temp]=None
                    
    return my_dict;
    

geo_data = '/home/kaisa/Documents/Python/GeoLite2/GeoLite2-City.mmdb' # CHANGE ROOT PATH

def latLongToDict(dbase, my_dict):
    reader = geoip2.database.Reader(dbase)
    for k in my_dict:
        my_dict[k]={}
        try:
            response = reader.city(k)
        except:
            pass
        else:            
            latitude = response.location.latitude
            my_dict[k]['lat']=latitude
            longitude = response.location.longitude
            my_dict[k]['long']=longitude
                    
    return my_dict;


def pointsFromDict(my_dict, my_map):
    temp_lat = 0.0
    temp_long = 0.0
    for k in my_dict:         
        if temp_lat == 0.0 and temp_long == 0.0:
                      
            if my_dict[k]!={}:
                latitude = float(my_dict[k]['lat'])
                longitude = float(my_dict[k]['long'])
                x,y = my_map(longitude, latitude)
                my_map.plot(x,y,'ro', markersize=4)
                temp_lat = latitude
                temp_long = longitude
            else:
                continue
                              
        else:
            latitude = float(my_dict[k]['lat'])
            longitude = float(my_dict[k]['long'])
            my_map.drawgreatcircle(temp_long, temp_lat, longitude,latitude)
            x,y = my_map(longitude, latitude)
            my_map.plot(x,y,'ro', markersize=4)
            temp_lat = latitude
            temp_long = longitude



def main(): 
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="enter a website")
    args = parser.parse_args()
    check_argument = str(check_output(["host", args.ip]), 'utf-8')
   
    if 'has address' in check_argument:
        tmp_out = check_output(["traceroute",args.ip])
        out = str(tmp_out, 'utf-8')
    else:
        print('Incorrect argument.')   
    print(ipToDict(out))
    plt.figure(figsize=(30,15))
    my_map = Basemap()
    my_map.drawcoastlines(color='grey')
    my_map.fillcontinents(color='grey')
    my_map.drawmapboundary(color='grey')
    pointsFromDict(latLongToDict(geo_data,ipToDict(out)), my_map) #makes my_map available
    plt.show()

#main()

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()