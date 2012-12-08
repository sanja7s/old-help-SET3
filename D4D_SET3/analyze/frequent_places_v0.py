'''
Created on Nov 29, 2012

@author: sscepano
'''
import sys
from multiprocessing import Pool
import numpy as np
from os import listdir
from os.path import isfile, join
import dateutil.parser


def fq_places(by_night = False, save_to_file = False):

    fq = np.zeros( (500001, 256) , dtype=int)
    D4DPath_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    
    i = 0
    
    for file_name in listdir(D4DPath_SET3):
        f_path = join(D4DPath_SET3,file_name)
        if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                usr = int(usr)
                subpref = int(subpref[:-1])
                # add night check
                if by_night == True:
                    dt = dateutil.parser.parse(call_time)
                    if dt.hour > 19 or dt.hour <= 5:
                        fq[usr][subpref] += 1
                else:
                    fq[usr][subpref] += 1
                
    if save_to_file == True:
        if by_night == True:
            store_file_name = 'SET3_Fq_calls_user_subprefs_night.tsv'
        else:
            store_file_name = 'SET3_Fq_calls_user_subprefs.tsv'
        file_store = open(store_file_name, "w")
        for usr in range (500001):
            for subpref in range (256):
                f = fq[usr][subpref]
                if f <> 0:
                    file_store.write(str(usr) + '\t' + str(subpref) + '\t' + str(f) + '\n')
        
        file_store.close()
    
    print (i)        
    return fq

def waiting():
    print 'waiting'
