#!/usr/bin/python

import sys
import heapq

#create heap queue
top_10_question = [ ]
heapq.heapify(top_10_question)

for line in sys.stdin:		# for ever line in the input from stdin
    line = line.strip()		# Remove trailing characters
    id, value = line.split("\t", 1)
    value = int(value)
            
    # populate into heapqueue
    heapq.heappush(top_10_question, (value, id))
            
    if len(top_10_question) > 10:		# more than 10 rows
        heapq.heappop(top_10_question)

#reverse the heap queue and print the result
for value, id in reversed([heapq.heappop(top_10_question) for x in range (len(top_10_question))]):
    id = id.strip(",")
    print("{0}\t{1}".format(value, id))
