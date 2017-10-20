#!/usr/bin/env python
from socket import *
import sys
import time
from datetime import *
from optparse import OptionParser
import re

#Variables
targetHost = ''
targetPort = ''
maxPortNum = 9999
minPortNum = 1
tp=[]

#Command-line switches to specify a host and port(s)
parser = OptionParser()
parser.add_option("-t", "--target", help="target host address")
parser.add_option("-p", "--port", help="target port")
(options, args) = parser.parse_args()
if not options.target:
	parser.error("Target host not given (-t [Target Host])")
if not options.port:
	parser.error("Target port(s) not given (-p [Port Number],[Port Number]")

#Scanner function
def myScanner(targetHost, targetPort, code = 1):
	try:
		connection = socket(AF_INET, SOCK_STREAM)
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
#print tp

print("Host: %s Port(s): %s" % (targetHost, targetPort))
print("Port scan started\n")

for ports in tp:
	try:
		response = myScanner(targetHost, ports)

		if response == 0:
			print("Port %d: \tOPEN" % (ports))
		else:
			print("Port %d: \tCLOSED" % (ports))
	except Exception, e:
		pass
