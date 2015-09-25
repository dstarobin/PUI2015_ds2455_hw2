# to run in command line, use: python get_bus_info.py <Your_APU_Key> <Bus Route e.g. M7> <csv output name e.g. M7.csv>

import json
import sys
import urllib2
import csv

#defining variables from command line args
API_key = sys.argv[1]
busroute = sys.argv[2]
csv_name = sys.argv[3]

if __name__ == '__main__':
    # accepts command line args for API key and bus line name (e.g. B61 etc.)
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}'.format(
        API_key, busroute)
    request = urllib2.urlopen(url)
    busdata = json.load(request)

    #creating variable to iterate over
    activity = busdata['Siri']['ServiceDelivery'][
        'VehicleMonitoringDelivery'][0]['VehicleActivity']
    
    #creates csv file from arg in command line with specified headers
    with open(sys.argv[3], 'wb') as csvFile:
        writer = csv.writer(csvFile)
        headers = ['Latitude', 'Longitude', 'Stop Name', 'Stop Status']
        writer.writerow(headers)

        #iterates over the variable to get coordinates of each bus
        for i in activity:
            latitude = i['MonitoredVehicleJourney'][
                'VehicleLocation']['Latitude']
            longitude = i['MonitoredVehicleJourney'][
                'VehicleLocation']['Longitude']
            
            #to generate stop/ distance info and NAs if nothing there 
            if i["MonitoredVehicleJourney"]["OnwardCalls"] == {}:
                stop_name = "N/A"
                stop_status = "N/A"
            else:
                stop_name = i['MonitoredVehicleJourney'][
                    'OnwardCalls']['OnwardCall'][0]['StopPointName']
                stop_status = i['MonitoredVehicleJourney']['OnwardCalls'][
                    'OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
            
            #writes above to csv
            writer.writerow([latitude, longitude, stop_name, stop_status])
