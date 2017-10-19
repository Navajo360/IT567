#!/usr/bin/env python
from socket import *
import sys, time
from datetime import datetime
from optparse import OptionParser

host = ''
max_port = 5000
min_port = 1

#Command-line switches to specify a host and port
parser = OptionParser()
parser.add_option("-t", "--target", help="target host address")
parser.add_option("-p", "--port", help="target port")
(options, args) = parser.parse_args()

def scan_host(host, port, r_code = 1):
	try:
		s = socket(AF_INET, SOCK_STREAM)
		
		code = s.connect_ex((host, port))

		if code == 0:
			r_code = code
		s.close()
	except Exception, e:
		pass

	return r_code

try:
	host = raw_input("Host address: ")
except KeyboardInterrupt:
	print("\n\n Application shutting down")
	sys.exti(1)

hostip = gethostbyname(host)
print("\nHost: %s IP: %s" % (host, hostip))
print("Scanning started at %s...\n" % (time.strftime("%H:%M:%S")))
start_time = datetime.now()

for port in range(min_port, max_port):
	try:
		response = scan_host(host, port)

		if response == 0:
			print("Port %d: OPEN" % (port))
	except Exception, e:
		pass

stop_time = datetime.now()
total_time_duration = stop_time - start_time
print("Scanning finished at %s ..." % (time.strftime("%H:%M:%S")))
print("Scanning duration: %s ..." % (total_time_duration))
print("Goodbye")
