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
#TCP Scanner function
def myTCPscanner(targetHost, targetPort, code = 1):
	try:
		connection = socket(AF_INET, SOCK_STREAM)
		connection.settimeout(0.5)
		myScannerCode = connection.connect_ex((targetHost, targetPort))
		if myScannerCode == 0:
			code = myScannerCode
		connection.close()
	except Exception, e:
		pass
	return code
#UDP Scanner function
def myUDPscanner(targetHost, targetPort, code = 1):
	try:
		connection = socket(AF_INET, SOCK_DGRAM)
		connection.settimeout(0.5)
		myScannerCode = connection.connect_ex((targetHost, targetPort))
		if myScannerCode == 0:
			code = myScannerCode
		connection.close()
	except Exception, e:
		pass
	return code
#mpr
def mpr(option, opt, value, parser):
	minPortNum = int(raw_input("Start Port: "))
	maxPortNum = int(raw_input("End Port: "))
	targetHost = parser.values.target
	th = []
	for j in targetHost.split(','):
		th += [j]

	print("Host(s): %s" % (th))
	print("\nPort scan started at %s" % (time.strftime("%H:%M:%S")))

	for hosts in th:
		print("\nHost: %s" % (hosts))
		for ports in range(minPortNum, maxPortNum):
			try:
				response = myTCPscanner(hosts, ports)

				if response == 0:
					print("Port %d: \tOPEN" % (ports))
			except Exception, e:
				pass
	print("\nPort scan finshed at %s" % (time.strftime("%H:%M:%S")))
	sys.exit()
#port1
def port1(option, opt, value, parser):
	targetHost = parser.values.target
	targetPort = parser.values.port
	th = []
	tp = []
	#Seperates the ports since they are added in a comma seperated list
	for i in targetPort.split(','):
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
#udp
def udp(option, opt, value, parser):
	targetHost = parser.values.target
	targetPort = parser.values.port
	th = []
	tp = []
	#Seperates the ports since they are added in a comma seperated list
	for i in targetPort.split(','):
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
				response = myUDPscanner(hosts, ports)

				if response == 0:
					print("Port %d: \tOPEN" % (ports))
				else:
					print("Port %d: \tCLOSED" % (ports))
			except Exception, e:
				pass
	print("\nPort scan finshed at %s" % (time.strftime("%H:%M:%S")))
	sys.exit()

#Command-line switches to specify host(s) and port(s)
parser = OptionParser()
parser.add_option("-t", "--target", help="target host address")
parser.add_option("-p", "--port", help="target port")
parser.add_option("-u", "--udp", help="udp scan", action="callback", callback=udp)
parser.add_option("-r", "--range", help="target port range", action="callback", callback=mpr)
(options, args) = parser.parse_args()
if not options.target:
	parser.error("Target host(s) not given (-t [Target Host],[Target Host])")
#if not options.port:
#	parser.error("Target port(s) not given (-p [Port Number],[Port Number]")
	
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



print("\nPort scan finshed at %s" % (time.strftime("%H:%M:%S")))
