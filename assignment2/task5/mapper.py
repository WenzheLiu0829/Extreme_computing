#!/usr/bin/python

import sys, random
from heapq import heappush, heapreplace

size = 1
resevoir = [ ]

for line in sys.stdin:
    line = line.strip()
    r = random.random()
    if len(resevoir) < size: 
       heappush(resevoir, (r, line))
    elif r > resevoir[0][0]: 
       heapreplace(resevoir, (r, line))

for (r, line) in resevoir:
    print('{0}\t{1}'.format(-r, line))
