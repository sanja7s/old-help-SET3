'''
Created on Nov 21, 2012

@author: sscepano
'''

import logging
import traceback
from multiprocessing import Pool
#from read_in import data as rd
from read_in import seq_mining_data as rd
#from analyze import night_homes as a
from analyze import seq_mining_weeks as a

#from visualize import graph_statistics as gs

_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')
    
    # Build a pool of 8 processes
    #pool = Pool(processes=8,)
    
    #c = ['A','B','C','D','E', 'F', 'G','H','I', 'J']
    #c = 'C'
    #data = pool.map(rd.read_in_file, c)
    #res = pool.map(nh.find_home,(data, c))
    
    #data = rd.read_in_file(c)
    #C = ['A','B','C','D','E', 'F', 'G','H','I', 'J']
        
    C = ['A']
    home_subprefs = [7]
    #data = {}
    
    #for  c in C:
        #data = rd.read_in_file(c, data)
        
    data = rd.read_in_file(C, home_subprefs)
    
    
    #_log.info("Data loaded.")
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            #reload(rd)
            reload(a)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            #a.find_home(pd.find_usr_call_fq(data))  
            #a.fq_places(by_night = True, save_to_file = True)
#            home = {}
#            home = a.find_home(data, home, c)
#            a.print_home('ALL', home)
            a.freq_seq(data)
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()