#!/usr/bin/python
import sys
import random
import linecache

linecache.clearcache()

filename = "/afs/inf.ed.ac.uk/group/teaching/exc/ex2/part3/webLarge.txt"
myfile = open(filename)
lines = len(myfile.readlines())

for i in range(100):
    n = random.randint(1,lines)
    output_line = linecache.getline(filename,n)
    output_line = output_line.strip()
    print(output_line)

