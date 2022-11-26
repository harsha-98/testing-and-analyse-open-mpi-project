import os
import re
dir = os.getcwd()
dir_n=dir+"\ompi-main"
print(dir_n)

file_count=0
l=[]
for path, subdirs, files in os.walk(dir_n):
    for f in files:
     count=0
     if(r'\test' not in path):
      #print("dfd",f)
      if(f.endswith(".c") or f.endswith(".h")):
       file_count+=1
       l.append(f)
       file_path = path + "\\" + f
       new_file = open(file_path, 'r+',encoding='UTF8')
       read_line = new_file.readlines()
       for lines in read_line:
        if(re.search("\s*(assert)\s*\([^\)]*\)", lines)):
         count+=1
       print(path,' , ',f,' , ',count)
#print("total no:",file_count)
print(len(l))
