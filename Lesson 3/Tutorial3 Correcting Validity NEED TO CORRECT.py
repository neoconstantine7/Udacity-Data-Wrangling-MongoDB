# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 11:39:35 2014

@author: changli
"""

#Lesson 3 CORRECTING VALIDITY 
"""
Your task is to check the "productionStartYear" of the DBPedia autos datafile for valid values.
The following things should be done:
- check if the field "productionStartYear" contains a year
- check if the year is in range 1886-2014
- convert the value of the field to be just a year (not full datetime)
- the rest of the fields and values should stay the same
- if the value of the field is a valid year in range, as described above,
  write that line to the output_good file
- if the value of the field is not a valid year, 
  write that line to the output_bad file
- discard rows (neither write to good nor bad) if the URI is not from dbpedia.org
- you should use the provided way of reading and writing data (DictReader and DictWriter)
  They will take care of dealing with the header.

You can write helper functions for checking the data and writing the files, but we will call only the 
'process_file' with 3 arguments (inputfile, output_good, output_bad).
"""
import csv
import pprint
import re

INPUT_FILE = 'autos.csv'
OUTPUT_GOOD = 'autos-valid.csv'
OUTPUT_BAD = 'FIXME-autos.csv'

def process_file(input_file, output_good, output_bad):

    with open(input_file, "r") as f: #input_file refers to source file name
        reader = csv.DictReader(f)  #read f
        header = reader.fieldnames

        #COMPLETE THIS FUNCTION
        bad_data = []
        good_data = []
        for line in reader: 
            value = line['productionStartYear']
            year_value = re.search(r'^\d\d\d\d', value) 
            #print year_value, value, line['URI']

            if 'dbpedia.org' not in line['URI']:
                continue
            if year_value is not None:
                if int(year_value.group()) in range(1886, 2015):
                    line['productionStartYear'] = int(year_value.group())
                    #print year_value.group(), type(year_value.group()), line['productionStartYear'], type(line['productionStartYear'])
                    #print line
                    good_data.append(line)
                else:
                    bad_data.append(line)
            else:
                bad_data.append(line)
        #print good_data
        #print bad_data
          
    # This is just an example on how you can use csv.DictWriter
    # Remember that you have to output 2 files
    with open(OUTPUT_GOOD, "w") as g:
        writer = csv.DictWriter(g, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in good_data:
            writer.writerow(row)

    with open(OUTPUT_BAD, "w") as h:
        writer = csv.DictWriter(h, delimiter=",", fieldnames= header)
        writer.writeheader()
        for row in bad_data:
            writer.writerow(row)     

def test():

    process_file(INPUT_FILE, OUTPUT_GOOD, OUTPUT_BAD)


if __name__ == "__main__":
    test()