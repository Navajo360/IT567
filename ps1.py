#!/usr/bin/env python
from socket import *
import sys
import time
from optparse import OptionParser

#Variables
targetHost = ''
targetPort = ''
maxPortNum = 9999
minPortNum = 1
tp = []
th = []

#Command-line switches to specify host(s) and port(s)
parser = OptionParser()
parser.add_option("-t", "--target", help="target host address")
parser.add_option("-p", "--port", help="target port")
(options, args) = parser.parse_args()
if not options.target:
	parser.error("Target host(s) not given (-t [Target Host],[Target Host])")
if not options.port:
	parser.error("Target port(s) not given (-p [Port Number],[Port Number]")

#Scanner function
def myTCPscanner(targetHost, targetPort, code = 1):
	try:
		connection = socket(AF_INET, SOCK_STREAM)
		connection.settimeout(2)
		myScannerCode = connection.connect_ex((targetHost, targetPort))
		if myScannerCode == 0:
			code = myScannerCode
		connection.close()
	except Exception, e:
		pass
	return code

targetHost = options.target
targetPort = options.port

#Seperates the ports since they are added in a comma seperated list
for i in targetPort.split(','):
	#print i
	tp += [int(i)]

#Seperates the hosts since they are added in a comma seperated list
for j in targetHost.split(','):
	th += [j]

print("Host(s): %s \nPort(s): %s" % (th, tp))
print("\nPort scan started at %s" % (time.strftime("%H:%M:%S")))

for hosts in th:
	print("\nHost: %s" % (hosts))
	for ports in tp:
		try:
			response = myTCPscanner(hosts, ports)

			if response == 0:
				print("Port %d: \tOPEN" % (ports))
			else:
				print("Port %d: \tCLOSED" % (ports))
		except Exception, e:
			pass

print("\nPort scan finshed at %s - %s" % (time.strftime("%H:%M:%S")))
