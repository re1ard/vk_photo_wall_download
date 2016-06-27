import urllib
import os
import time
from timeout import timeout

name = '64259879'



f = open(name,'r')

repeat = 3
i = 0


rootdir = os.getcwd() + '/'

@timeout(15)
def save(photolink):
	try:
		urllib.urlretrieve(photolink, rootdir + photolink.split('/')[len(photolink.split('/'))-1].split('\n')[0])
                i = i + 1
		print photolink + ' loaded! ' + str(i)
		repeat = 3
	except Exception as msg:
		repeat = repeat - 1
		if repeat == 0:
			pass
		print msg
		save(photolink)

while 1:
	for photolink in f:
		try:
			save(photolink)
		except:
			pass
		time.sleep(0.1)
	print "down"
	break
