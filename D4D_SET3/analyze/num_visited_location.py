'''
Created on Dec 8, 2012

@author: sscepano
'''
import numpy as n
import pyplot as plt

# for gives group of user ids and for the input file it will find probability of number of visited places
# the last argument enables to use this function cumulatively over the time period invoking it iteratively
def find_funct_and_avg(usr_group, c):
    
    # here for each user we store the number of visited places
    usr_places_cum = n.zeros((500001, 256), dtype=n.int)
    # from the previous array obtained by dividing by the total number of users in user group
    prob_place_usrs = n.zeros(256)
    
    
    for letter in c:
        file_name = "SET3_Fq_calls_user_subprefs_SUBPREF_POS_SAMPLE_" + chr(letter) + ".TSV"
        # open given file which has frequencies of calls of each user per each subpref 
        # from which they called in the time period
        # also initialize needed arrays
        f = open(file_name, 'r')    
        # read the file and num of places visited for each user
        for line in f:
            usr_id, subpref, visits = line.split('\t')
            usr_id = int(usr_id)
            subpref = int(subpref)
            usr_places_cum[usr_id][subpref] += 1
            
        # this array gets populated for each number of places visited -- by the total number of users who have 
        # that many visited places
        place_usrs = n.zeros(500001, dtype=n.int)
    
        # populate place with additional users who visited that many places
        for usr in usr_group:
            num = n.count_nonzero(usr_places_cum[usr])
            place_usrs[num] += 1
        
        # avg = 0
            
        for places in range(256):
            prob_place_usrs[places] = place_usrs[places] / float(len(usr_group))
            print(prob_place_usrs[places]) 
        
        plt.plot(prob_place_usrs, marker='.', label= str((letter-ord('A')+1)*2) + ' weeks')
        
    file_name = "SET3_Fq_calls_user_subprefs.tsv"
    f = open(file_name, 'r')
    usr_places = n.zeros(500001, dtype=n.int)
    place_usrs = n.zeros(256, dtype=n.int)
    prob_place_usrs = n.zeros(256)
    
    for line in f:
        usr_id, subpref, visits = line.split('\t')
        usr_id = int(usr_id)
        usr_places[usr_id] += 1
    
    for usr in usr_group:
        num = usr_places[usr]
        place_usrs[num] += 1
        
    for places in range(256):
        prob_place_usrs[places] = place_usrs[places] / float(len(usr_group))
        print(prob_place_usrs[places])

    plt.plot(prob_place_usrs, label= 'TOTAL')
        
    plt.yscale('log')
    plt.xscale('log')
    plt.xlim(0, 256)
    plt.xlabel('N subprefs visited')
    plt.ylabel('P(N)')
    plt.legend()    
    plt.show()
            
    #  avg =  avg / len(usr_group)    
    # print avg 
    
    return usr_places_cum, prob_place_usrs 
    

def superimpose_plot(usr_grp):
        
    c = range(ord('A'), ord('J')+1)    
    usr_places_cum, prob_place_usrs = find_funct_and_avg(usr_grp, c)



usr_grp = range(1,500000)
superimpose_plot(usr_grp) 