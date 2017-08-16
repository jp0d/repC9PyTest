#!/usr/bin/python
# prints the active variables and their type and available functions

for i in dir():
	print i + ' : ' + str(type(i))
	for j in dir(i):
		print '\t' + j

