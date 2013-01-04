'''
Created on Dec 20, 2012

@author: sscepano
'''
import numpy as n

def save_usr_calling_fq(unc):
    
    fileout = '/home/sscepano/D4D res/SET3 frequent callers from python/Usr_call_fq.tsv'
    fileout2 = '/home/sscepano/D4D res/SET3 frequent callers from python/Usr_num_calls.tsv'
    ucf = n.zeros(500001)
    fout = open(fileout, 'w')
    fout2 = open(fileout2, 'w')
    
    hrs = 7.0*24.0*2.0*10.0
    for usr in range(500001):
        fout2.write(str(usr) + '\t' + str(unc[usr]) + '\n')
        ucf[usr] = unc[usr] / hrs
        fout.write(str(usr) + '\t' + str(ucf[usr]) + '\n')
    
    fout.close()
    fout2.close()
    print('All users num calls saved to file ' + fileout)
    print('All fq saved to file ' + fileout)    
    return ucf




def filter_fq_callers(unc, fq):
    fq = 0
    fileout = '/home/sscepano/D4D res/SET3 frequent callers from python/FQ_callers_' + str(fq) + '.tsv'
    fileout2 = '/home/sscepano/D4D res/SET3 frequent callers from python/FQ_callers_NUMCALLS' + str(fq) + '.tsv'
    ucf = n.zeros(500001)
    fout = open(fileout, 'w')
    fout2 = open(fileout2, 'w')
    uf = {}
    i = 0
    print(len(unc))
    hrs = 7.0*24.0*2.0*10.0
    for usr in range(500001):
        ucf[usr] = unc[usr] / hrs
        if ucf[usr] >= fq:
            uf.keys().append(usr)
            uf[usr] = unc[usr]        
            i = i + 1
            fout.write(str(usr) + '\t' + str(ucf[usr]) + '\n')
            fout2.write(str(usr) + '\t' + str(unc[usr]) + '\n')

    fout.close()
    fout.close()
    
    return uf
  
    