#!/usr/bin/python

"""
csv-to-db.py
@author:        Piotr Jedra
@date:          Aug-2019
This program reads a CSV file and saves its content to a database of choice

Usage py csv-to-db.py -f [file], i.e. py csv-to-db.py -f "sample.csv" 
"""

import sys # usage print(sys.argv[1])
import os
import argparse
#import mysql.connector # mySQL
#import pymongo # MongoDb
import csv


# argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", required = False, help = "Path to the csv file")
args = vars(ap.parse_args())

#connect with the database - mySQL
#mydb = mysql.connector.connect(host="localhost", user="user", passwd="password")
#cursor = mydb.cursor()
#cursor.execute("USE database")

#connect with the database - MongoDb
#myclient = pymongo.MongoClient("mongodb://localhost:27017")
#mydb = myclient["mydatabase"]
#mycol = mydb["parts_time"]


with open(args['file']) as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    line_count = 0
    if csv.Sniffer().has_header: #check if the csv file has a line with headers, if so then ignore the first line
        next(readCSV)
    for row in readCSV:
        line_count += 1
        if row:
            print(row)
            #myList = [[date_2,row[1],row[2],row[3],date_4]]
            #mycol.insert_many(myList)
            
            #cursor.execute("INSERT INTO parts_time (time_id,time_day,time_month,time_year,vendor_idk) VALUES (%s,%s,%s,%s,%s)" % tuple([date_2,row[1],row[2],row[3],date_4]))
    print(f'Processed {line_count} lines.')