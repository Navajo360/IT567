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
parser.add_option("-p", "--port", help="target port", type="int")
(options, args) = parser.parse_args()
if not options.target:
	parser.error("Target host not given")
if not options.port:
	parser.error("Target port(s) not given")

#Scan function
def myscanner(host, port, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		
		code = s.connect_ex((host, port))
		
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

for port in range(targetPort, targetPort):
	try:
		up = myscanner(targetHost, targetPort)
		if up == 0:
			print("Port %s: Open" % (targetPort))
	except Exception, e:
		pass

print("Scan completed")
