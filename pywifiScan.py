# -*- coding: utf-8 -*-
import pywifi
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

while 1:
	iface.scan()
	time.sleep(1)
	results = iface.scan_results()

	signalNum = 0
	for result in results:
		if 'iphone'==result.ssid:
			print(result.ssid, result.signal)
		
		
		
		
		
		