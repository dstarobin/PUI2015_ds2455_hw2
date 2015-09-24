#This script retrieves/ reports info about locations of all active vehicles on one MTA bus line
#my API key = 4280fc9e-4ec8-4106-ba00-6c4cc71597d3
#full url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=4280fc9e-4ec8-4106-ba00-6c4cc71597d3&VehicleMonitoringDetailLevel=calls&LineRef=B63'
#to use in command line: python show_bus_locations.py <BusTime API key> <Bus route #, e.g. B52>

import json
import sys
import urllib2

API_key = sys.argv[1]
busroute = sys.argv[2]

if __name__=='__main__':
  #accepts command line args for API key and bus line name (e.g. B61 etc.)
	url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}'.format (API_key, busroute)
	request = urllib2.urlopen(url)
	busdata = json.load(request)

	activity = busdata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

	num_buses = 0
	for i in activity:
		num_buses += 1

	print "Bus Line: %s" % (sys.argv[2])	
	print "Number of Active Buses:", num_buses

	print_count = 0
		
	for i in activity:
		print_count += 1
		latitude = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'] 
		longitude = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		print "Bus %s is at latitude %s, longitude %s." % (print_count, latitude, longitude)
