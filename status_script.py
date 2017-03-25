#! /usr/bin/python

import subprocess
import time
from datetime import datetime

now = datetime.now()
date = str(now.year)+' '+str(now.month)+' '+str(now.day)
doc = open(str(now)+'.txt','a+')
doc.write(str(date)+'\nTime;Temperature;CPU-usage\n\n')


# Method to get the total CPU-usage at this moment
def getCpuUsage():
        cpuUsage = 0
        command = 'top -b -n 1'
        respons = subprocess.Popen(command)
        print respons


# Method to get the temperature of the CPU at this moment
def getTemp():
        command = 'sensors'
        temp = subprocess.check_output(command)[56:60]
        return temp

	
while True :
	now = datetime.now()
	timestamp = str(now.hour)+':'+str(now.minute)+':'+str(now.second)

	temp = getTemp()
#	getCpuUsage()
	string = timestamp+';'+temp+'\n'
	doc.write(string)
	time.sleep(1)

doc.close()
