#this example reads and prints CO2 equiv. measurement, TVOC measurement, and temp every 2 seconds

from time import sleep
from Adafruit_CCS811 import Adafruit_CCS811

ccs =  Adafruit_CCS811()

while not ccs.available():
	pass
temp = ccs.calculateTemperature()
ccs.tempOffset = temp - 25.0
if ccs.available():
	temp = ccs.calculateTemperature()
	if not ccs.readData():
		print ('{"CO2":',ccs.geteCO2(),",",'"ppmTVOC":',ccs.getTVOC(),",",'"temp":',temp,"}"
else:
	print ("ERROR!")
