from os import listdir
from os.path import isfile, join
import os
import shutil;

class Manager:
	extension = ["pdf","docx","doc","xlxs","pptx","xlsx"];

	def doExist(self,extent):
		for i in Manager.extension:
			if(extent==i):
				return True;
		return False;

	def work(self):
		mypath = os.getcwd()
		path = mypath;
		onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
		for i in onlyfiles:
			if(len(i.split("."))>1):
				str = i.split(".")[1]	
			if(self.doExist(str)):
				if(os.path.exists(path+"/"+str)):
					shutil.move(mypath+"/"+i,mypath+"/"+str)
				else:
					os.mkdir(str)
					shutil.move(mypath+"/"+i,mypath+"/"+str)
			#print(i.split(".")[1])	

m =  Manager()
m.work();