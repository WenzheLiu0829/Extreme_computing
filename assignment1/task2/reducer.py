#!/usr/bin/python

import sys

prev_word = ""
value_total = 1
word = ""
flag = 1

for line in sys.stdin:          # For ever line in the input from stdin
    line = line.strip()         # Remove trailing characters
    word = line.split("\n")
    value = 1 
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_word == word:
        value_total += value
        flag = 0
    else:
        if prev_word and flag ==1 :  # write result to stdout
           print(prev_word[0])
        value_total = value
        prev_word = word
        flag = 1
if prev_word and flag ==1 :  # write result to stdout
   print(prev_word[0])
