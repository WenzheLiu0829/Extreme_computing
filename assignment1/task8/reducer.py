#!/usr/bin/python

import sys


student_name = ''
dict = {}
studentID = ""
prev_name = ""
prev_ID = ""
count = 1
grad_dict = {}
score_total = 0

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    prev_ID,word = line.split("\t", 1)
    word = word.split()

    if studentID == prev_ID: #the same student
       if word[0] == "mark":
          dict[word[1]] = word[2]
          count += 1
       else:
          student_name = word[1]
    else:
       if prev_ID : #an old student ends
          if count > 3:
             for k,v in dict.iteritems():
                 v = int(v)
                 score_total += v
             score_ave = score_total / float(count)
             grad_dict[score_ave] = student_name
             score_total = 0
          dict = { }
          count = 1
       if word[0] == "mark":
          dict[word[1]] = word[2]
       else:
          student_name = word[1]
       studentID = prev_ID

if studentID == prev_ID:
   if count > 3:
      for k,v in dict.iteritems():
          v = int(v)
          score_total += v 
      score_ave = score_total / float(count)
      grad_dict[score_ave] = student_name

grad_dict =  sorted(grad_dict.iteritems(), key=lambda asd:asd[0] , reverse=True)
name = grad_dict[0]
print(name[1])
