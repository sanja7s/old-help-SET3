'''
Created on Dec 12, 2012

@author: sscepano
'''
import datetime
#region_subpref_map = {}
#
#file_name = "/home/sscepano/DATA SET7S/Region_subprefs_mapping.csv"
#f = open(file_name, 'r')    
#for line in f:
#    region_id, subpref_id = line.split('\t')
#    region_id = int(region_id)
#    subpref_id = int(subpref_id[:-1])
#    try:
#        region_subpref_map[region_id].append(subpref_id)
#    except KeyError:
#        region_subpref_map[region_id] = [subpref_id]
#        
##for i in region_subpref_map.iterkeys():
##    print(region_subpref_map[i])
#
#non = []
#
#for i in range(1,255):
#    not_found = True
#    found = False
#    for j in region_subpref_map.iterkeys():
#        if i in region_subpref_map[j] and found == True:
#            print ('found twice ' + str(i))
#        if i in region_subpref_map[j] and found == False:
#            not_found = False
#            found = True
#            #print ('found ' + str(i))
#            #break
#    if not_found:
#        non.append(i)
#        print ('NOT found ' + str(i))
#        
#print (non)

print(datetime.date(2011,12,1).isocalendar()[1])
