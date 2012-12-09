'''
Created on Dec 8, 2012

@author: sscepano
'''
import numpy as n
import pyplot as plt

def plot_and_avg(usr_group):
    
    file_name = "SET3_Fq_calls_user_subprefs.tsv"
    f = open(file_name, 'r')
    usr_places = n.zeros(500001, dtype=n.int)
    place_usrs = n.zeros(256, dtype=n.int)
    prob_place_usrs = n.zeros(256)
    
    for line in f:
        usr_id, subpref, visits = line.split('\t')
        usr_id = int(usr_id)
        usr_places[usr_id] += 1
        
    avg = 0
    
    for usr in usr_group:
        num = usr_places[usr]
        avg += num
        place_usrs[num] += 1
        
    for places in range(256):
        prob_place_usrs[places] = place_usrs[places] / float(len(usr_group))
        print(prob_place_usrs[places]) 
        
    avg =  avg / len(usr_group)    
    print avg 
    
    #print(place_usrs)  
    
    plt.plot(prob_place_usrs)
    plt.yscale('log')
    plt.xscale('log')
    plt.show()


usr_grp = range(1,500000)
plot_and_avg(usr_grp) 