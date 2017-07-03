#!/usr/bin/python
import sys

approved_answer = None

for line in sys.stdin:		# for every line in the input from stdin
    line = line.strip()		# Remove trailing characters
    keys, user_id = line.split("\t", 1)
    answer_id, type_id = keys.split(" ", 1)
    user_id = int(user_id)
    answer_id = int(answer_id)
    type_id = int(type_id)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if type_id == 1:		# question
        approved_answer = answer_id	# mark that it is approved answer
    elif type_id == 2:    	# answer
        if answer_id == approved_answer:	# the answer is approved answer
            print("{0}\t{1}".format(user_id, answer_id))
