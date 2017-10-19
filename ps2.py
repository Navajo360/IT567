#!/usr/bin/env python
from socket import *
import sys
import time
from datetime import *
from optparse import OptionParser

#Variables
targetHost = ''
targetPort = ''
maxPortNum = 9999
minPortNum = 1


#Command-line switches to specify a host and port
parser = OptionParser()
parser.add_option("-t", "--target", help="target host address")
parser.add_option("-p", "--port", help="target port")
(options, args) = parser.parse_args()
#Scan function
def myscanner(targetHost, targetPort, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		
		code = s.connect_ex((targetHost, targetPort))
		
		if code == 0:
			r_code = code
		s.close()
	except Exception, e:
		pass
		
	return r_code
#try:
#	host = raw_input("Target Host IP: ")
#except KeyboardInterrupt:
#	print("Shutting Down")
#	sys.exit(1)
targetHost = options.target
targetPort = options.port
print("Host: %s Port: %s" % (targetHost, targetPort))
print("Port scan started\n")

up = myscanner(targetHost, targetPort)
if up == 0:
	print("Port %s: Open" % (targetPort))

print("Scan completed")
