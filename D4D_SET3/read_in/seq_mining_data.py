'''
Created on Dec 14, 2012

@author: sscepano
'''
from os.path import isfile, join
from datetime import date, timedelta
import numpy as np

def read_in_file(C, home_subprefs):
    
    i = 0
    #data = defaultdict(int)
    data = np.zeros((20,7,256), dtype=int) 
#    for i in range(20):
#        for j in range (7):
#            data[i][j] = []

    file_name1 = "Users_divided_by_home_subprefALL.tsv"
    f1 = open(file_name1, 'r')
    usr_grp = np.zeros(500001)
    for line in f1:
        line = line.rstrip().split('\t')
        subpref1 = int(line[0][:-1])
        if subpref1 in home_subprefs:
            for i in range(1, len(line)):
                usr_grp[int(line[i])] = 1

    print 'check'
   
    for c in C:
        D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
        file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
        f_path = join(D4D_path_SET3,file_name)
        if isfile(f_path) and file_name != '.DS_Store':
                file7s = open(f_path, 'r')
                for line in file7s:
                    i = i + 1
                    print i
                    usr, call_time, subpref = line.split('\t')
                    subpref = int(subpref[:-1])
                    usr = int(usr)
                    if usr_grp[usr] == 1:
                        call_date = date(int(call_time[:4]), int(call_time[5:7]), int(call_time[8:10]))
                        data[call_date.isocalendar()[1]-48][call_date.weekday()][subpref] = 1
                
    print i            
    return data