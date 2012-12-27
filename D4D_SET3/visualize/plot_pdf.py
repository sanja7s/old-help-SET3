'''
Created on Dec 19, 2012

@author: sscepano
'''
def plot_intervals_fq(N, interval, c):
    
    import pyplot as plt
    import numpy as n
    plt.figure(10)
    N = float(N)
    fq_interval = n.zeros(3360)

    for j in range(0, 3360):
        fq_interval[j] = interval[j] / N
        
    file_name = "/home/sscepano/D4D res/SET3 intervals from python/SET3 call interval counts " + c + ".tsv"
    #file_name = "/home/sscepano/D4D res/SET3 intervals from python/SET3 call interval fq " + c + ".tsv"
    f = open(file_name,'w')    
    
    for j in range(0, 3360):
        f.write(str(j) + '\t' + str(interval[j]) + '\n')
        #f.write(str(j) + '\t' + str(fq_interval[j]) + '\n')

    plt.plot(interval, color= 'green',label= 'count, set ' + c)
    #plt.plot(fq_interval, label= 'pdf I, set ' + c)

    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('Interval between calls [hr]')
    #plt.ylabel('Count I')
    plt.ylabel('P(I)')
    plt.legend()    
    #plt.show()
    figure_name = "/home/sscepano/D4D res/SET3 intervals from python/SET3 count intervals between calls " + c + ".png"
    #figure_name = "/home/sscepano/D4D res/SET3 intervals from python/SET3 pdf intervals between calls 2" + c + ".png"
    print(figure_name)
    plt.savefig(figure_name, format = "png")        

    return
    