#!/usr/bin/python

import sys
import heapq

prev_user_id = None
user_id = None
question_id = None
question_list = [ ]

#create th heapqueue
top_user = [ ]
heapq.heapify(top_user)
heapq.heappush(top_user, (0, 0, 0))	# init heapqueue

for line in sys.stdin:		# for every line in the input from stdin
    line = line.strip()		# Remove trailing characters
    user_id, question_id = line.split("\t", 1)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_user_id == user_id:		#same user_id
        question_list.append(question_id)

    else:
        if prev_user_id:  # pop to heap queue
            heapq.heappushpop(top_user, (len(question_list), prev_user_id, question_list))

        prev_user_id = user_id
        question_list = [ ]
        question_list.append(question_id)

if prev_user_id == user_id:  # Don't forget the last (key,value) pair
    heapq.heappushpop(top_user, (len(question_list), prev_user_id, question_list))

#get the most user who answered question and print
total_quest, user_id, question_list = heapq.heappop(top_user)
print("{0}\t{1}".format(user_id, ', '.join(question_list)))
