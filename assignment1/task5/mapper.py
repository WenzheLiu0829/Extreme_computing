#!/usr/bin/python

import sys

def get_three_sequences(tokens,num):
    for i in range(num-1):
        a = tokens[i]
        b = tokens[i+1]
        c = tokens[i+2]
        d = " "
        end = tokens[-1]
        e = a + d + b + d + c
        print("{0}\t{1}".format(e, 1))

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    tokens = line.split()
    sentence = str(tokens)
    num = len(sentence) - len(sentence.replace(' ',''))
    get_three_sequences(tokens,num)
