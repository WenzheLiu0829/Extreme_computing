#!/usr/bin/python

import sys
import hashlib
import BitVector
from math import log
from math import ceil

class BloomFilter():

    def __init__(self, size, hash_num):
        self.size = size
        self.bitset = BitVector.BitVector(size=self.size)
        self.hash_num = hash_num

    def insert(self, value):
        md5 = hashlib.md5()
        for f in range(self.hash_num):
            md5.update(value)
            loc = long(md5.hexdigest(),16) % self.size
            self.bitset[loc] = 1
    def isContaions(self, value):
        if value == None:
           return False
        ret = True
        md5 = hashlib.md5()
        for f in range(self.hash_num):
            md5.update(value)
            loc = long(md5.hexdigest(),16) % self.size
	    ret = ret & self.bitset[loc]
        return ret

n = int(sys.argv[1]) #number of items in the filter
p = 0.01 #probability of false positives
m = ceil((n * log(p)) / log(1.0 / (pow(2.0, log(2.0))))) #number of bits in the filter
k = round(log(2.0) * m / n)       # number of hash functions

bf = BloomFilter( int(m),int(k))

for line in sys.stdin:                  # input from standard input
    line = line.strip()                 # remove whitespaces
    if bf.isContaions(line) == False:
	print(line)
	bf.insert(line)
