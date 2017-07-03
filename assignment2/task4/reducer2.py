#!/usr/bin/python

import sys
import heapq

prev_user_id = None
answers = []

#create the heapqueue
top_user = [ ]
heapq.heapify(top_user)
heapq.heappush(top_user, (0, 0, 0))	# headpqueue init

for line in sys.stdin:		# for ever line in the input from stdin
    line = line.strip()		# Remove trailing characters
    user_id, answer_id = line.split("\t", 1)
    user_id = user_id.strip()
    answer_id = answer_id.strip()
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_user_id == user_id:		#same user_id
        answers.append(answer_id)
    else:
        if prev_user_id:  # populate to heap queue
            heapq.heappushpop(top_user, (len(answers), prev_user_id, answers))

        prev_user_id = user_id
        answers = []
        answers.append(answer_id)

if prev_user_id == user_id:  # Don't forget the last (key,value) pair
    heapq.heappushpop(top_user, (len(answers), prev_user_id, answers))

#get and print the result
total_answers, user_id, answers = heapq.heappop(top_user)
answers.sort()			#sort the answers id list
print("{0}\t-> {1}\t{2}".format(user_id, total_answers, ', '.join(answers)))
