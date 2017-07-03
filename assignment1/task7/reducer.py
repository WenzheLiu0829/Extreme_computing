#!/usr/bin/python

import sys


student_name = ''
dict = {}
studentID = ""
prev_name = ""
prev_ID = ""

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    prev_ID,word = line.split("\t", 1)
    word = word.split()    

    if studentID == prev_ID: #the same student
       if word[0] == "mark":
          dict[word[1]] = word[2]
       else:
          student_name = word[1]
    else:
       if prev_ID and student_name!="" : #an old student ends
          str = student_name+" -->"
          for k,v in dict.iteritems():  
              str += "(" 
	      str += k
              str += ","
              str += v
              str += ") "
          print(str)
          str = ""
       dict = {}
       if word[0] == "mark":
          dict[word[1]] = word[2]
       else:
          student_name = word[1]
       studentID = prev_ID

if studentID == prev_ID:
   str = student_name+" -->"
   for k,v in dict.iteritems():
       str += "("
       str += k
       str += ","
       str += v
       str += ") "
   print(str)
