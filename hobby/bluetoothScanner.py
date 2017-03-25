import bluetooth

myPhone = 'Thomas sin iPhone'
myAddr = None

nearby_devices = bluetooth.discover_devices(lookup_names = True)

for addr, name in nearby_devices:
	print name,addr
		
nrOfDevices = len(nearby_devices)

if nrOfDevices == 0:
	s = '\nThere are none devices with Bluetooth turned on '
elif nrOfDevices == 1:
	s = '\nThere are %i device with Bluetooth turned on. ' %(nrOfDevices)
else:
	s = '\nThere are %i devices with Bluetooth turned on. ' %(nrOfDevices)
	
# Over 70% of users have Bluetooth enabled, source http://www.emergingmarketer.com/book/chapter6/6-5.html read 19.3.2013
people = nrOfDevices*1.3

s += 'This will indicate that there are %i persons around you now.' %(people)
print s