'''
Created on Nov 30, 2012

@author: sscepano
'''
from collections import OrderedDict

def find_home(data, home, c):
    
    for usr in data.keys():
        #print(data[usr])
        #data[usr] = OrderedDict(sorted(data[usr].items(), key=lambda t: t[1], reverse=True)) 
        home[usr] = home.get(usr, {})
        for ant in data[usr]:
            try:
                home[usr][ant] += data[usr][ant]
            except KeyError:
                home[usr][ant] = data[usr][ant]
        #home[usr] = data[usr].popitem()
        #f.write(str(usr) + '\t' + str(data[usr]) + '\n')
        home[usr] = OrderedDict(sorted(home[usr].items(), key=lambda t: t[1], reverse=True)) 
        
    return home



def print_home(c, home):
    
    fileout = 'Stats_No_Users_per_home_subpref_v2' + c  + '.tsv'
    f = open(fileout, 'w')
    division = {}
    for usr in home:
        #f.write(str(usr) + ';\t')
        try:
            ant = home[usr].popitem(last=False)[0]
        except KeyError:
            break
            #f.write(str(ant) + ':\t' + str(home[usr][ant]) + '\t')
        try:
            division[ant].append(usr)
        except KeyError:
            division[ant] = [usr]    
        #f.write('\n')
  
    for ant in division.iterkeys():
        division[ant] = len(division[ant])
    
    
    division = OrderedDict(sorted(division.items(), key=lambda t: t[1], reverse=True))
        
    for ant in division.iterkeys():
        f.write(str(ant) + '\t')
        f.write(str(division[ant]))
        f.write('\n')
    f.close()