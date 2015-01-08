#!/usr/bin/python
__author__ = 'Brandon'
__verssion__ = '1.1'

from datetime import datetime
import csv

#TRAIN
#inputfile = 'D:\\Kaggle Click-Through\\train\\train.csv'
#outputfile = 'D:\\Kaggle Click-Through\\train\\train.vw'
#train = 'True'

#TEST
inputfile = 'D:\\Kaggle Click-Through\\test\\test.csv'
outputfile = 'D:\\Kaggle Click-Through\\test\\test.vw'
train = 'False'

vw_data_line = ""
file_write_counter=0

total = 0
f = open(outputfile, 'wb')

start = datetime.now()
print('\nInput File: '+inputfile)
print('\nOutput File: '+outputfile)
print('\nBeginning VW Conversion Process\n')

with open(inputfile) as csv_file:
    reader = csv.DictReader(csv_file)
    for e, row in enumerate(reader):

        # add predictor / label if training
        if train == "True":

            if row['click'] == "1":
                vw_data_line = vw_data_line + "1 "
            else:
                vw_data_line = vw_data_line + "-1 "
        #add record / row identifier
        vw_data_line = vw_data_line + "'" + str(row['id']) + " "

        #begin numerical / non-factor namespace variables
        vw_data_line = vw_data_line + "|i "
        vw_data_line = vw_data_line + "C14:" + str(row['C14']) + " "
        vw_data_line = vw_data_line + "C15:" + str(row['C15']) + " "
        vw_data_line = vw_data_line + "C16:" + str(row['C16']) + " "
        vw_data_line = vw_data_line + "C17:" + str(row['C17']) + " "
        vw_data_line = vw_data_line + "C18:" + str(row['C18']) + " "
        vw_data_line = vw_data_line + "C19:" + str(row['C19']) + " "
        vw_data_line = vw_data_line + "C20:" + str(row['C20']) + " "
        vw_data_line = vw_data_line + "C21:" + str(row['C21']) + " "

        #begin categorical / factor variables
        vw_data_line = vw_data_line + "|c "
        vw_data_line = vw_data_line + str(row['C1']) + " "
        vw_data_line = vw_data_line + str(row['banner_pos']) + " "
        vw_data_line = vw_data_line + str(row['site_id']) + " "
        vw_data_line = vw_data_line + str(row['site_domain']) + " "
        vw_data_line = vw_data_line + str(row['site_category']) + " "
        vw_data_line = vw_data_line + str(row['app_id']) + " "
        vw_data_line = vw_data_line + str(row['app_domain']) + " "
        vw_data_line = vw_data_line + str(row['app_category']) + " "
        vw_data_line = vw_data_line + str(row['device_id']) + " "
        vw_data_line = vw_data_line + str(row['device_model']) + " "
        vw_data_line = vw_data_line + str(row['device_type']) + " "
        vw_data_line = vw_data_line + str(row['device_conn_type']) + " "
        vw_data_line = vw_data_line + str(row['hour'])
        vw_data_line = vw_data_line + '\n'

        #add line break

        f.write(vw_data_line)
        vw_data_line = ""
        if e % 1000000 == 0:
            print("%s\t%s"%(e, str(datetime.now() - start)))


f.close()
print("\n %s Task execution time:\n\t%s"%(e, str(datetime.now() - start)))