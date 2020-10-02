import requests
import socket
import sys

url='http://'+sys.argv[1];
with open(sys.argv[2],'r') as word:
	wordlist=[line.strip() for line in word.read().split('\n') if line]

for i in wordlist:
	s=requests.get(url+'/'+i)
	if(s.status_code==404):
		continue;
	else:
		print("/{0}: {1}".format(i,s.status_code))

