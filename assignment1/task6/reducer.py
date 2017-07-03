#!/usr/bin/python
import sys
import math

prev_word = ""
value_total = 0
word = ""
dict = {}
flag = 0
index = 1
logx = 0
list = []

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    word,value = line.split("\t")
    value = int(value)
    if prev_word == word: #the same data
        value_total += value
        index += 1
        list.append(value)
    else:
	if prev_word:  # write result to stdout
           for i in range(index):
               tmp = list[i] / float(value_total)
               logx += tmp * (math.log(tmp,2))
           logx = -logx
           print("{0}:{1}".format(prev_word,logx))
        index= 1
        logx = 0
        list = []
        value_total = value
        prev_word = word
        list.append(value)
if prev_word == word:  # Don't forget the last key/value pair
   for i in range(index):
       tmp = list[i] / float(value_total)
       logx += tmp * (math.log(tmp,2))
   logx = -logx
   print("{0}:{1}".format(prev_word,logx))
