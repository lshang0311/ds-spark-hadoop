#!/usr/bin/env python

import sys
import csv

SEP = "\t"


class Mapper:

    def __init__(self, stream, sep=SEP):
        self.stream = stream
        self.sep = sep

    def emit(self, key, value):
        sys.stdout.write("{}{}{}\n".format(key, self.sep, value))

    def map(self):
        for row in self:
            self.emit(row[3], row[6])

    def __iter__(self):
        reader = csv.reader(self.stream)
        for row in reader:
            yield row


if __name__ == '__main__':
    mapper = Mapper(sys.stdin)
    # f = open('flights.csv', 'r')
    # mapper = Mapper(f)
    mapper.map()

