import pandas as pd
import csv
import sys
import numpy as np

#header = ("ID", "Date")

#df = csv.reader(open('/Users/shadiferris/Desktop/python/datecsv.csv', 'r'), delimiter=",")

with open('/Users/shadiferris/Desktop/python/datecsv.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        #print(row[0])
        #print(row[0],row[1],row[2],)

d1 = raw_input('Enter date - ')

for row in readCSV:
    #if current rows 2nd value is equal to input, print that row
        if d1 == row[1]:
	print row[0]
#d1 = int(row[0)]
#df = csv.reader(open('/Users/shadiferris/Desktop/python/datecsv.csv', 'r'), delimiter=",")

#d2 = raw_input('Enter another  date - ')

#for row in mylist:
 # if d2 == row[1]:
        #print row[0]
#d2 = int(row[0])
#print(int(d2(row[0]) - d1(row[0])))
