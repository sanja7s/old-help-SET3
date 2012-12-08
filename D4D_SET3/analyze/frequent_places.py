'''
Created on Nov 29, 2012

@author: sscepano
'''
import sys
from multiprocessing import Pool
import numpy as np
from os import listdir
from os.path import isfile, join

def read_in_file(c):
    
    i = 0
    data = []
    
    D4D_path_SET3 = "/home/sscepano/DATA SET7S/D4D/SET3TSV"
    file_name = "SUBPREF_POS_SAMPLE_" + c + ".TSV"
    f_path = join(D4D_path_SET3,file_name)
    if isfile(f_path) and file_name != '.DS_Store':
            file7s = open(f_path, 'r')
            for line in file7s:
                i = i + 1
                usr, call_time, subpref = line.split('\t')
                call_hour = int(call_time[11:13])
                if call_hour > 19 or call_hour <= 5:
                    data.append(((usr, subpref),1))
    
    print i            
    return data

def Partition(data):
    tf = {}
    for sublist in data:
        for p in sublist:
            try:
                tf[p(0)].append(p)
            except KeyError:
                tf[p[0]] = [p]
    return tf
    
def Reduce(Mapping):
    return (Mapping[0], sum(pair[1] for pair in Mapping[1]))

def tuple_sort(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return cmp(a[0], b[0])
    
def chunks(l, n):
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

if __name__ == '__main__':
    # Build a pool of 8 processes
    pool = Pool(processes=8,)
    
    #text = []
    
    #for c in xrange(ord('A'), ord('J')+1):
    c = ['A','B','C','D','F', 'G','H', 'J']
    text = pool.map(read_in_file, c)
        #print(len(data))
    
    
    #c = 'A'
    #data = read_in_file('A')
    #print(len(data))
    #partitioned_text = list(chunks(text, len(text) / 8))
        
#    tuples = Partition(partitioned_text)
#    
#    freq = pool.map(Reduce, tuples.items())
#    
#    freq.sort (tuple_sort)
#        
#    
#    for pair in freq[:20]:
#        print pair[0], ":", pair[1]


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
                    call_hour = int(call_time[11:13])
                    if call_hour > 19 or call_hour <= 5:
                        #data.append(((usr, subpref),1))
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

def wait():
    print 'wait'