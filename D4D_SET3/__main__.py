'''
Created on Nov 21, 2012

@author: sscepano
'''

import logging
import traceback
import numpy as n

from multiprocessing import Pool
from read_in import data as rd
from analyze import fq_calling_users as a

_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')
        
    C = ['A','B','C','D','E','F','G','H','I','J']
    data = n.zeros(500001, dtype=n.int)
    
    for  c in C:
        data = rd.read_in_whole_file(c, data)
    
    _log.info("Data loaded.")
    fq_data = a.save_usr_calling_fq(data)
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            reload(a)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            fq = 0.2
            a.filter_fq_callers(fq_data, fq)
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()