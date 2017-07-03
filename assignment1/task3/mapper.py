#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    #tokens = line.split('\n')               # split the line into tokens

    #for token in tokens:                # write the results to standard output
    print(line)
