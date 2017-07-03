#!/usr/bin/python

import sys
import heapq

question_id = [ ]

# create the heapqueue
top_user = [ ]
heapq.heapify(top_user)
heapq.heappush(top_user, (0, 0, 0))	# init heapqueue

for line in sys.stdin:		# for every line in the input from stdin
    line = line.strip()		# Remove trailing characters
    user_id, value = line.split("\t", 1)
    question_id = value.strip().split(", ")

    # push and pop into the heapqueue
    heapq.heappushpop(top_user, (len(question_id), user_id, question_id))
    question_id = [ ]

total_quest, user_id, question_id = heapq.heappop(top_user)
question_id.sort()			# sort the question list
print("{0}\t-> {1}".format(user_id, ', '.join(question_id)))
