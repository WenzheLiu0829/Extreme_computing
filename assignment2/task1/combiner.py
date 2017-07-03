#!/usr/bin/python
import sys

prev_word = None
prev_file = None
value_total = 0
word = None
filename = None

for line in sys.stdin:		# for every line in the input from stdin
    line = line.strip()		# Remove trailing characters
    keys, value = line.split("\t", 1)
    word, filename = keys.split(" ", 1)
    value = int(value)
    # Remember that Hadoop sorts map output by key combiner takes these keys sorted
    if prev_word == word:
        if prev_file == filename:	#the same filename based on the same word
            value_total += value	
        else:				#different filename but the same word
            if prev_file:		
		print("{0} {1}\t{2}".format(prev_word, prev_file, value_total))
            value_total = value
            prev_file = filename
    else: # different word
        if prev_word:  
	    print("{0} {1}\t{2}".format(prev_word, prev_file, value_total))
        value_total = value
        prev_word = word
        prev_file = filename

if prev_word == word:  # Don't forget the last key/value pair
    print("{0} {1}\t{2}".format(prev_word, prev_file, value_total))
