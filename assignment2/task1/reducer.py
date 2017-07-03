#!/usr/bin/python
import sys

prev_word = None
prev_file = None
word = None
filename = None
files = [ ]
count_file = 0
value_total = 0

for line in sys.stdin:		# for ever line in the input from stdin
    line = line.strip()		# Remove trailing characters
    keys, value = line.split("\t", 1)
    word, filename = keys.split(" ", 1)
    value = int(value)
    # Remember that Hadoop sorts map output by key reducer takes these keys sorted
    if prev_word == word:		# the same word
        if prev_file == filename:	# same filename based on the same word
            value_total += value
        else:                           # different filenames but the same word
            if prev_file:
                count_file += 1         # count the number of file
                files.append("({0}, {1})".format(prev_file, value_total)) #append the file to the list
            value_total = value
            prev_file = filename

    else:                               # different words
        if prev_word:  
            count_file += 1     
            files.append("({0}, {1})".format(prev_file, value_total))
            print ("{0}\t: {1}\t: {2}".format(prev_word, count_file, '{'+', '.join(files)+'}'))            

        count_file = 0
        prev_word = word
        prev_file = filename
        files = [ ]
        value_total = value

if prev_word == word:  # Don't forget the last key/value pair
    count_file += 1
    files.append("({0}, {1})".format(prev_file, value_total))
    print("{0}\t: {1}\t: {2}".format(prev_word, count_file, '{'+', '.join(files)+'}'))
