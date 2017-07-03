#!/usr/bin/python

import sys

for line in sys.stdin:		# input from standard input
    line = line.strip()		# remove whitespaces

    post_type = line[line.find(" PostTypeId=")+13:][:line[line.find(" PostTypeId=")+13:].find('"')]
    if post_type == "1":	# question row
       q_id = line[line.find(" Id=")+5:][:line[line.find(" Id=")+5:].find('"')]
       view_count = line[line.find(" ViewCount=")+12:][:line[line.find(" ViewCount=")+12:].find('"')]
       print("{0},\t{1}".format(q_id, view_count))
