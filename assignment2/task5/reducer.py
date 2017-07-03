#!/usr/bin/python
import sys

size = 1
count = 0

for line in sys.stdin:
    line = line.strip()
    (size, line) = line.split('\t')
    print(line)
    count += 1
    if count == size: 
       break
