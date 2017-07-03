#!/usr/bin/python

import sys

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    tokens = line.split()               # split the line into tokens
    tmp = tokens[1]
    tokens[1] = tokens[0]
    tokens[0] = tmp
    print("{0}\t{1}".format(tokens[0],' '.join(map(str,tokens[1:]))))
