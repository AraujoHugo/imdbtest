rfile = open('../tt2333784','r')

for line in rfile:
	cenas = line.split()
	print cenas[1],"http://web.archive.org/web/"+cenas[1]+"/"+cenas[2]
