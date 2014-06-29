#!/usr/bin/python

import cgi
import cgitb




def writeFile(info):
	text_file = open("LatLongReport.txt", "w")
	text_file.write(info + "\n")


cgitb.enable()

writeFile("cenas")
