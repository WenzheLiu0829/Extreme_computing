#!/usr/bin/python

import sys

def get_two_sequences(tokens):
    a = tokens[0]
    b = tokens[1]
    value = tokens[3]
    d = ' '
    e = a + d + b
    print("{0}\t{1}".format(e,value))

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    tokens = line.split()
    get_two_sequences(tokens)
