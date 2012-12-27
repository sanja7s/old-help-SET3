'''
Created on Nov 21, 2012

@author: sscepano
'''

import logging
import traceback
import numpy as n
from multiprocessing import Pool
from read_in import times_between_calls as rd
from visualize import plot_pdf as a

_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')
    
    c = 'E'
    interval = n.zeros(3360)
    N, interval = rd.read_in_file(c, interval)
    
    _log.info("Data loaded.")
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            #reload(rd)
            reload(a)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            # THIS THE FUNCTION YOU ARE TESTING
            a.plot_intervals_fq(N, interval, c)
            
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == '__main__':
    main()