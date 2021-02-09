#Script by Mert TANRIVER 
#Scraper for WEB-GL Models

import numpy as np
import linecache
import os
import time

fread = open("input.txt")
fwrite = open("final.txt", "a")

print("/****** Process Began Successfully ******/")
print("Percentage = %0 --> Input file is being read ")
while True: 
    line = fread.readline(2) 

    if line == "vt":
        fvt = open("vt.txt", "a")
        fvt.write(fread.readline(-1))

    if line == "vn":
        fvn = open("vn.txt", "a")
        fvn.write(fread.readline(-1))  
    
    if line == "v ":
        fv = open("v.txt", "a")
        fv.write(fread.readline(-1)) 
    

    if line == "f ":
        fq = open("f.txt", "a")
        fq.write(fread.readline(-1)) 

    if not line: 
        break
    
print("Percentage = %25 --> Removing the spaces")

fwrite.close()
fread.close()
fvt.close()
fvn.close()
fv.close()
fq.close()

v_count = 0
vt_count = 0
vn_count = 0
f_count = 0

f = open("v.txt", 'r')
f2 = open("v2.txt", 'a')
f.seek(0)
lines = f.readlines()
for line in lines:
    f2.write(line[1:])
    v_count += 1
f.close()
f2.close()

f = open("vt.txt", 'r')
f2 = open("vt2.txt", 'a')
f.seek(0)
lines = f.readlines()
for line in lines:
    f2.write(line[1:])
    vt_count += 1
f.close()
f2.close()

f = open("vn.txt", 'r')
f2 = open("vn2.txt", 'a')
f.seek(0)
lines = f.readlines()
for line in lines:
    f2.write(line[1:])
    vn_count += 1
f.close()
f2.close()

f = open("f.txt", 'r')
f2 = open("f2.txt", 'a')
f.seek(0)
lines = f.readlines()
for line in lines:
    f2.write(line[:])
    f_count += 1
f.close()
f2.close()

print("Percentage = %50 --> Adding commas")

fv2 = open("v2.txt", "r")
b = fv2.readlines()
a = ''.join(b)
a = a.replace(' ', ',')
a = a.replace('\n', ',\n')
print("Percentage = %65")
fv2.close()

text_file = open("V-Output.txt", "a")
text_file.write("/* *** V Attributes *************************************************************/\n")
text_file.write("var vertices = [")
text_file.write(a)
text_file.write("];\n")
text_file.write("/*"+ str(v_count) + " lines*/")
text_file.write("\n\n\n\n\n\n\n\n\n")
text_file.close()

fv2 = open("vn2.txt", "r")
b = fv2.readlines()
a = ''.join(b)
a = a.replace(' ', ',')
a = a.replace('\n', ',\n')
print("Percentage = %75")
fv2.close()

text_file = open("VN-Output.txt", "a")
text_file.write("/* *** VN Attributes ************************************************************/ \n")
text_file.write("var normals = [")
text_file.write(a)
text_file.write("];\n")
text_file.write("/*"+ str(vn_count) + " lines*/")
text_file.write("\n\n\n\n\n\n\n\n\n")
text_file.close()

fv2 = open("vt2.txt", "r")
b = fv2.readlines()
a = ''.join(b)
a = a.replace(' ', ',')
a = a.replace('\n', ',\n')
print("Percentage = %85")
fv2.close()

text_file = open("VT-Output.txt", "a")
text_file.write("/* *** VT Attributes ************************************************************/ \n")
text_file.write("var textureCoords = [")
text_file.write(a)
text_file.write("];\n")
text_file.write("/*"+ str(vt_count) + " lines*/")
text_file.write("\n\n\n\n\n\n\n\n\n")
text_file.close()

fv2 = open("f2.txt", "r")
b = fv2.readlines()
a = ''.join(b)
a = a.replace(' ', ',')
a = a.replace('/', ',')
a = a.replace('\n', ',\n')
a = a.replace(',,\n', ',\n')
print("Percentage = %95")
fv2.close()

text_file = open("F-Output.txt", "a")
text_file.write("/* *** F Attributes *************************************************************/  \n")
text_file.write("var quads = [")
text_file.write(a)
text_file.write("];\n")
text_file.write("/*"+ str(f_count) + " lines*/")
text_file.write("\n\n\n\n\n\n\n\n\n")
text_file.close()

print("Percentage = %99")
print("Removing the leftover files...")

os.remove("v.txt")
os.remove("v2.txt")
os.remove("vn.txt")
os.remove("vn2.txt")
os.remove("vt.txt")
os.remove("vt2.txt")
os.remove("f.txt")
os.remove("f2.txt")
os.remove("final.txt")

fwrite.close()
fread.close()

print("Percentage = %100")
print("Task successfully ended")
print("The results are in the '*-Output.txt' files")
print("Exiting...")
time.sleep(5)
