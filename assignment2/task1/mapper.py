#!/usr/bin/python

import sys
import os

for line in sys.stdin:          # input from standard input
    line = line.strip()         # remove whitespaces
    tokens = line.split()       # split the line into tokens

    for token in tokens:        # write the result to standard output
        #use the os method to get the filename
        filename = os.path.basename(os.environ["mapreduce_map_input_file"])
        print("{0} {1} {2}".format(token, filename, 1))
