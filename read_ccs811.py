#!/usr/bin/python
from Adafruit_CCS811 import Adafruit_CCS811

ccs =  Adafruit_CCS811()

while not ccs.available():
	pass
temp = ccs.calculateTemperature()
ccs.tempOffset = temp - 25.0

if ccs.available():
	    temp = ccs.calculateTemperature()
	    if not ccs.readData():
	       print ('{"CO2":', ccs.geteCO2(), ",", '"ppmTVOC":', ccs.getTVOC(), ",", '"temp":',temp,"}")

	    else:
	      print ("ERROR!")
