#!/usr/bin/python

import sys

linelen = 0
tokenlen = 0

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    words = line.split()
    if len(line)>linelen:
       linelen = len(line)
    for word in words:
        if len(word)>tokenlen:
           tokenlen = len(word)
print("linelen:",linelen)
print("tokenlen:",tokenlen)

