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
if not options.target:
	parser.error("Target host not given")
if not options.port:
	parser.error("Target port(s) not given")

#Scanner function
