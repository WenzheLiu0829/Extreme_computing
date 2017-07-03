#!/usr/bin/python

import sys
import re

for line in sys.stdin:		# input from standard input
    line = line.strip()		# remove whitespaces

    post_type = line[line.find(" PostTypeId=")+13:][:line[line.find(" PostTypeId=")+13:].find('"')]    

    if post_type == "2":	# answers
       if line.find("OwnerUserId=")>=0 and line.find("ParentId=")>=0:
          user_id = line[line.find(" OwnerUserId=")+14:][:line[line.find(" OwnerUserId=")+14:].find('"')]
          ques_id = line[line.find(" ParentId=")+11:][:line[line.find(" ParentId=")+11:].find('"')]
          print("{0}\t{1}".format(user_id, ques_id))
