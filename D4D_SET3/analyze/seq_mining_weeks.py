'''
Created on Dec 14, 2012

@author: sscepano
'''
import numpy as n

def freq_seq(data):
    
    items = n.zeros(256, dtype=int)
    
#    data1 = n.zeros((2,7,256), dtype=int)
#    for i in range (2):
#        for j in range(7):
#            for k in range(256):
#                data1[i][j][k] = int(data[i][j][k])
                
    for i in range (2):
        for j in range(7):
            for k in range(256):
                if data[i][j][k] == 1:
                    items[k] += 1
               
            
    print(items)
    return items 
        