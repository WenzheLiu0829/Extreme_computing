#!/usr/bin/python

import sys

for line in sys.stdin:          # input from standard input
    line = line.strip()         # remove whitespaces

    post_type = line[line.find(" PostTypeId=")+13:][:line[line.find(" PostTypeId=")+13:].find('"')]

    if post_type == "1":        # question
       if line.find("AcceptedAnswerId=")>=0: 
          answer_id = line[line.find(" AcceptedAnswerId=")+19:][:line[line.find(" AcceptedAnswerId=")+19:].find('"')]
          print("{0} {1} {2}".format(answer_id, post_type, 1))

    elif post_type == "2":	# answer
         answer_id = line[line.find(" Id=")+5:][:line[line.find(" Id=")+5:].find('"')]
         if line.find("OwnerUserId=")>=0:
            user_id = line[line.find(" OwnerUserId=")+14:][:line[line.find(" OwnerUserId=")+14:].find('"')]
            print("{0} {1} {2}".format(answer_id, post_type, user_id))
