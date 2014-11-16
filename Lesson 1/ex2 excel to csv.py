# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 11:58:10 2014

@author: changli
"""

######Lesson 1 exercise 2 Excel to CSV my approach        
import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = []
    row = []
    for n in range (1,sheet.ncols-1): #(1,8)
        station = sheet.cell_value(0,n)
        column_data = sheet.col_values(n, start_rowx=1, end_rowx = sheet.nrows+1)
        max_load = max(column_data)
        max_index = column_data.index(max_load)
        maxtime = xlrd.xldate_as_tuple(sheet.cell_value(max_index+1,0),0)
        row = [station, maxtime[0],maxtime[1],maxtime[2], maxtime[3], max_load]
        data.append(row)
    
    return data

data = parse_file(datafile)

def save_file(data, filename):
    with open(filename, "w") as f:
       # open file 
       resultFile = csv.writer(f, delimiter = '|')
       #if you want to make it csv readable, 
       #change delimiter to ','
       resultFile.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
       for item in data:
            resultFile.writerow(item) 
            # resultFile.writerow([item,]) will only work if there is one row . 
            # Otherwise, it will add bracket to the output, i.e. make the output another list
       
save_file(data, "test.csv")

    
#Lesson 1 exercise 2 Excel to CSV  standard answer
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = {}
    # process all rows that contain station data
    for n in range (1, 9):
        station = sheet.cell_value(0, n)
        cv = sheet.col_values(n, start_rowx=1, end_rowx=None)

        maxval = max(cv)
        maxpos = cv.index(maxval) + 1
        maxtime = sheet.cell_value(maxpos, 0)
        realtime = xlrd.xldate_as_tuple(maxtime, 0)
        data[station] = {"maxval": maxval,
                         "maxtime": realtime}

    print data
    return data

def save_file(data, filename):
    with open(filename, "w") as f: #output filename
        w = csv.writer(f, delimiter='|')
        w.writerow(["Station", "Year", "Month", "Day", "Hour", "Max Load"])
        for s in data:
            year, month, day, hour, _ , _= data[s]["maxtime"]
