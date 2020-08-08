import os as ls
import shutil
path = ls.getcwd()

data =ls.listdir(path)

for i in data:
    s1 =  i.split(".")
    if(len(s1)<2):
        continue
    if(s1[1]=="py"):
        print("found"+i)
        source = ls.path.join(ls.getcwd(),i)
        dist = ls.path.join(ls.getcwd(),"python")

        if not ls.path.exists(dist):
            ls.mkdir(dist)
            shutil.move(source,dist)
        if ls.path.exists(path):
            shutil.move(source,dist)

    if(s1[1]=="pdf"):
        print("found"+i)
        source = ls.path.join(ls.getcwd(),i)
        dist = ls.path.join(ls.getcwd(),"pdfdoc")
        if ls.path.exists(path):
            shutil.move(source,dist)

    if(s1[1]=="docx" or s1[1]=="doc"):
        print("found"+i)
        source = ls.path.join(ls.getcwd(),i)
        dist = ls.path.join(ls.getcwd(),"doc")
        if ls.path.exists(path):
            shutil.move(source,dist)

    if(s1[1]=="xlsx"):
        print("found"+i)
        source = ls.path.join(ls.getcwd(),i)
        dist = ls.path.join(ls.getcwd(),"excell")
        if ls.path.exists(path):
            shutil.move(source,dist)
