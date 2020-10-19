#!/usr/bin/env python

import csv
import sys

#header = ("ID", "Date")

df = csv.reader(open('/Users/shadiferris/Desktop/python/datecsv.csv', 'r'), delimiter=",")

d1 = input('Enter date - ')

for row in df:
    #if current rows 2nd value is equal to input, print that row
    if d1 == row[1]:
        d1_id = row[0]
        print(row[0])
#d1 = int(row[0)]

df = csv.reader(open('/Users/shadiferris/Desktop/python/datecsv.csv', 'r'), delimiter=",")

d2 = input('Enter another  date - ')

for row in df:
    if d2 == row[1]:
        d2_id = row[0]
        print(row[0])
#d2 = int(row[0])

calc1 = int(d1_id) - int(d2_id)

print(calc1)
