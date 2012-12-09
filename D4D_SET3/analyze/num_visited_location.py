'''
Created on Dec 8, 2012

@author: sscepano
'''
import numpy as n
import pyplot as plt

# for gives group of user ids and for the input file it will find probability of number of visited places
# the last argument enables to use this function cumulatively over the time period invoking it iteratively
def find_funct_and_avg(usr_group, file_name, usr_places_cum):
    
    # open given file which has frequencies of calls of each user per each subpref 
    # from which they called in the time period
    # also initialize needed arrays
    f = open(file_name, 'r')
    # this array gets populated for each number of places visited -- by the total number of users who have 
    # that many visited places
    place_usrs = n.zeros(500001, dtype=n.int)
    # from the previous array obtained by dividing by the total number of users in user group
    prob_place_usrs = n.zeros(256)
    
    # read the file and num of places visited for each user
    for line in f:
        usr_id, subpref, visits = line.split('\t')
        usr_id = int(usr_id)
        usr_places_cum[usr_id] += 1
        
    avg = 0
    
    # populate place with additional users who visited that many places
    for usr in usr_group:
        num = usr_places_cum[usr]
        place_usrs[num] += 1
        
    for places in range(256):
        prob_place_usrs[places] = place_usrs[places] / float(len(usr_group))
        print(prob_place_usrs[places]) 
        
    avg =  avg / len(usr_group)    
    print avg 
    
    return usr_places_cum, prob_place_usrs 
    

def superimpose_plot(usr_grp):
    
    prob_place_usrs = n.zeros((10, 256))
    # here for each user we store the number of visited places
    usr_places_cum = n.zeros((500001, 256), dtype=n.int)
    
    for c in range(ord('A'), ord('J')+1):
        file_name = "SET3_Fq_calls_user_subprefs_SUBPREF_POS_SAMPLE_" + chr(c) + ".TSV"
        usr_places_cum, prob_place_usrs[c-ord('A')] = find_funct_and_avg(usr_grp, file_name, usr_places_cum)
        
    for c in range(ord('A'), ord('J')+1):    
        plt.plot(prob_place_usrs[c-ord('A')], marker='.', label= str((c-ord('A')+1)*2) + ' weeks')
        
    file_name = "SET3_Fq_calls_user_subprefs.tsv"
    usr_places_TOTAL = n.zeros(500001, dtype=n.int)
    prob_place_usrs_TOTAL = find_funct_and_avg(usr_grp, file_name, usr_places_TOTAL)
    plt.plot(prob_place_usrs_TOTAL, marker='s', label= 'TOTAL')
    
    plt.yscale('log')
    plt.xscale('log')
    plt.xlim(0, 256)
    plt.xlabel('N subprefs visited')
    plt.ylabel('P(N)')
    plt.legend()
    plt.show()


usr_grp = range(1,500000)
superimpose_plot(usr_grp) 