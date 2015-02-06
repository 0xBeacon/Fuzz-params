#!/usr/bin/python

import httplib
n = 1
outfile=open("results.txt", "a")
while n<=100:
	conn = httplib.HTTPConnection("www.google.com")
	url = "/python/index.php?id="+str(n)
	conn.request('GET', url)
	resp = conn.getresponse()
	print resp.getheader("Server")
	print resp.getheader("Date")
	print resp.getheader("Cookie")
	respcode=resp.status
	result=url+" "+str(respcode)+"\n"
	outfile.write(result)
	n+=1
