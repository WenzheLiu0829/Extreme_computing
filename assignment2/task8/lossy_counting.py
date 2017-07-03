#!/usr/bin/python
import sys
from collections import defaultdict

n = 0
count = defaultdict(int)
bucket_id = {}
epsilon = 1e-3
current_bucket_id = 1

total_count = 0

for line in sys.stdin:
    line = line.strip()

    #add new line into count
    n += 1
    if line not in count:
       bucket_id[line] = current_bucket_id - 1
    count[line] += 1

    # do the trim
    if n % int(1 / epsilon) == 0:
       for content, total in count.items():
           if total <= current_bucket_id - bucket_id[content]:
              del count[content]
              del bucket_id[content]
       current_bucket_id += 1

#print the output
for content, total in count.iteritems():
    if (float(total)/n > 0.009):
       print("{0}\t{1}".format(total,content))
