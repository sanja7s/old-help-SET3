'''
Created on Dec 20, 2012

@author: sscepano
'''
from os.path import isfile, join
from datetime import date,timedelta, datetime

def read_in_file(c, interval):
    
    i = 0
    old_usr = 0
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                usr, call_time, subpref = line.split('\t')
                #subpref = subpref[:-1]
                usr = int(usr)
                if usr <> old_usr:
                    old_usr = usr
                    start = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
#                    start_call_hour = int(call_time[11:13])
#                    start_date = date(int(call_time[:4]), int(call_time[5:7]), int(call_time[8:10]))
                else:
                    i = i + 1
                    end = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
                    delt = end - start
                    delt = delt.days * 24 + delt.seconds / 3600
                    interval[delt] += 1
                    start = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
    
    print i            
    return i, interval

#call_time = '2011-12-02 14:49:00'
#date_object = datetime.strptime(call_time, '%Y-%m-%d %H:%M:%S')
#print date_object
#call_time2 = '2011-12-02 10:29:00'
#call_time1 = '2011-12-02 07:21:00'
#date_object1 = datetime.strptime(call_time1, '%Y-%m-%d %I:%M:%S')
#date_object2 = datetime.strptime(call_time2,'%Y-%m-%d %I:%M:%S')
#delt = date_object2 -date_object1
#print delt
#print delt.seconds
#print (delt.seconds / 3600)
#print delt > timedelta(hours=4)
#print(delt.seconds)
#print date_object2
#print date_object1