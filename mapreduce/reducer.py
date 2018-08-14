#!/usr/bin/env python

"""
A Reducer in Python that is memory efficient by using iterators.
"""

import sys
from itertools import groupby
from operator import itemgetter

SEP = "\t"


class Reducer:

    def __init__(self, infile=sys.stdin, separator=SEP):
        self.infile = infile
        self.sep = separator

    def emit(self, key, value):
        sys.stdout.write("{}{}{}\n".format(key, self.sep, value))

    def reduce(self):
        for current, group in groupby(self, itemgetter(0)):
            total = 0
            count = 0

            for item in group:
                total += item[1]
                count += 1
            self.emit(current, float(total) / float(count))

    def __iter__(self):
        for line in self.infile:
            try:
                parts = line.split(self.sep)
                yield parts[0], float(parts[1])
            except:
                continue


if __name__ == "__main__":
    TEST = False 

    reducer = Reducer(sys.stdin)
    if TEST:
        f = open('test_reducer.csv', 'r')
        reducer = Reducer(f)

    reducer.reduce()
