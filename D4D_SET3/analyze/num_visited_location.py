'''
Created on Dec 8, 2012

@author: sscepano
'''
import numpy as n
import pop_density as pop

# for given group of user ids and for the input file it will find probability of number of visited places
# the last argument enables to use this function cumulatively over the time period invoking it iteratively
def plot_distributions(usr_group, c, grp_type, grp_id):
    
    import pyplot as plt
    plt.figure(grp_id)
    
    print grp_id 
    
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
            #print(prob_place_usrs[places]) 
        
        plt.plot(prob_place_usrs, marker='.', label= str((letter-ord('A')+1)*2) + ' weeks')
        
#    file_name = "SET3_Fq_calls_user_subprefs.tsv"
#    f = open(file_name, 'r')
#    usr_places = n.zeros(500001, dtype=n.int)
#    place_usrs = n.zeros(256, dtype=n.int)
#    prob_place_usrs = n.zeros(256)
#    
#    for line in f:
#        usr_id, subpref, visits = line.split('\t')
#        usr_id = int(usr_id)
#        usr_places[usr_id] += 1
#    
#    for usr in usr_group:
#        num = usr_places[usr]
#        place_usrs[num] += 1
#        
#    for places in range(256):
#        prob_place_usrs[places] = place_usrs[places] / float(len(usr_group))
#        print(prob_place_usrs[places])
#
#    plt.plot(prob_place_usrs, label= 'TOTAL')
        
    plt.yscale('log')
    plt.xscale('log')
    plt.xlim(0, 256)
    plt.xlabel('N subprefs visited')
    plt.ylabel('P(N)')
    plt.legend()    
    #plt.show()
    figure_name = "/home/sscepano/D4D res/distr of num of visited subprefs/SET3_num_visited_places_distribution_" + grp_type + str(grp_id) + ".png"
    print(figure_name)
    plt.savefig(figure_name, format = "png")        
    #  avg =  avg / len(usr_group)    
    # print avg 
    
    return usr_places_cum, prob_place_usrs 
    

def superimpose_plot(usr_grp, grp_type, subpref):
        
    c = range(ord('A'), ord('J')+1)    
    usr_places_cum, prob_place_usrs = plot_distributions(usr_grp, c, grp_type, subpref)

def usr_grp_subprefs(subprefs):
    #usr_grp = range(1,500000)
    #subprefs = range(1,255)
    total_usr_grp = []
    
    file_name = "Users_divided_by_home_subprefALL.tsv"
    f = open(file_name, 'r')
    for line in f:
        usr_grp = []
        line = line.rstrip().split('\t')
        subpref = int(line[0][:-1])
        if subpref in subprefs:
            print 'found_' + str(subpref)
            for i in range(1, len(line)):
                usr_grp.append(int(line[i]))
                total_usr_grp.append(int(line[i]))
                #print(usr_grp)
            #superimpose_plot(usr_grp, subpref) 
    return total_usr_grp

def usr_grp_regions(regions):

    #regions = range(1,19)
    usrs = []
    region_subprefs = {}
    
    file_name = "/home/sscepano/DATA SET7S/D4D/SET3TSV/Region_subprefs_mapping.tsv"
    f = open(file_name, 'r')
    for line in f:
        region, subpref = line.rstrip().split('\t')
        region = int(region)
        subpref = int(subpref)
        if region in regions:
            try:
                region_subprefs[region].append(subpref)
            except KeyError:
                region_subprefs[region] = [subpref]
                
    for region in region_subprefs.iterkeys():
        usr_grp = usr_grp_subprefs(region_subprefs[region]) 
        usrs += usr_grp
            
    return usrs

# single region test
#region = 1
#usr_grp = usr_grp_regions([region])
#print(usr_grp)
#superimpose_plot(usr_grp,'REGION_',region)

# all regions create
#regions = range(1,19)
#for region in regions:
#    usr_grp = usr_grp_regions([region])
#    print(usr_grp)
#    superimpose_plot(usr_grp,'REGION_',region)

# regions grouped by pop density
regions = pop.divide_regions_by_pop_density()
print(regions['low'])
print(regions['medium'])
print(regions['high'])
#low_regions = regions['low']
#usr_grp = usr_grp_regions(low_regions)
#print(usr_grp)
#superimpose_plot(usr_grp,'REGIONS_LOW_DENSITY',len(low_regions))
#
#mid_regions = regions['medium']
#usr_grp = usr_grp_regions(mid_regions)
#print(usr_grp)
#superimpose_plot(usr_grp,'REGIONS_MEDIUM_DENSITY',len(mid_regions))
#
#high_regions = regions['high']
#usr_grp = usr_grp_regions(high_regions)
#print(usr_grp)
#superimpose_plot(usr_grp,'REGIONS_HIGH_DENSITY',len(high_regions))   

         