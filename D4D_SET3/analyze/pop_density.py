'''
Created on Dec 13, 2012

@author: sscepano
'''

def divide_regions_by_pop_density():
    
    regions_by_dens = {'low': [], 'medium': [], 'high': []}
    
    file_name = "/home/sscepano/DATA SET7S/D4D/SET3TSV/Pop_region_density.tsv"
    f = open(file_name, 'r')
    for line in f:
        region, dens = line.rstrip().split('\t')
        region = int(region)
        dens = int(dens)
        if dens < 40:
            regions_by_dens['low'].append(region)
        elif dens < 100:
            regions_by_dens['medium'].append(region)
        else:
            regions_by_dens['high'].append(region)
        
    return regions_by_dens