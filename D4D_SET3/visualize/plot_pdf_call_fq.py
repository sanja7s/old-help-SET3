'''
Created on Dec 19, 2012

@author: sscepano
'''

def plot_pdf_postgres_out(file_name):
    
    import pyplot as plt
    plt.figure(1)
    import numpy as n

    
    # here we store the number of calls made by a user
    num_calls = n.zeros(500001, dtype=n.int)
    # from the previous array obtained by dividing by the total number of users in user group
    num_users = n.zeros(500001, dtype=n.int)
    
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        nc, nu = line.split('\t')
        nc = int(nc)
        nu = int(nu)
        num_calls[i] = nc
        num_users[i] = nu

    mi = min(num_calls)
    mx = max(num_calls)
    print(mi)
    print(mx)
    
    fq_calls = n.zeros(500001)
    total_hrs = float(24*7*20)
    
    for j in range(0, 500001):
        fq_calls[j] = num_calls[j] / total_hrs
        #fq_calls[j] = num_calls[j] 
    
    percent_users = n.zeros(500001)
    total_u = float(sum(num_users))
    
    for j in range(0, 500001):
        percent_users[j] = num_users[j] / total_u
        #percent_users[j] = num_users[j]
    
#    plt.plot(num_calls, num_users, label= 'prob distribution of frequency of calls')
    plt.plot(fq_calls, percent_users, label= 'pdf fq calls')
        

        
#    plt.yscale('log')
#    plt.xscale('log')
#    plt.xlim(0, 256)
    plt.xlabel('N, fq calls')
    plt.ylabel('P(N)')
    plt.legend()    
    #plt.show()
    figure_name = "/home/sscepano/D4D res/SET3 frequent callers from python/SET3 ONLY FQ distr of fq of calls.png"
    print(figure_name)
    plt.savefig(figure_name, format = "png")        
#    #  avg =  avg / len(usr_group)    
#    # print avg 
    
    return
    

plot_pdf_postgres_out("/home/sscepano/D4D res/SET3 frequent callers from python/Only_FQ_callers_0.25.tsv")


def plot_pdf_python_out(file_name):
    
    import pyplot as plt
    plt.figure(1)
    import numpy as n

    
    # here we store the number of calls made by a user
    fq_calls = n.zeros(500001)
    # from the previous array obtained by dividing by the total number of users in user group
    num_users = n.zeros(500001, dtype=n.int)
    
    i = 0
    f = open(file_name, 'r')    
    # read the file
    for line in f:
        i = i + 1
        nu, nc = line.split('\t')
        nc = float(nc)
        nu = int(nu)
        fq_calls[i] = nc
        num_users[i] = nu

    mi = min(fq_calls)
    mx = max(fq_calls)
    print(mi)
    print(mx)
    
#    for j in range(0, 500001):
#        #fq_calls[j] = num_calls[j] / total_hrs
#        fq_calls[j] = fq_calls[j] 
    
    percent_users = n.zeros(500001)
    total_u = float(sum(num_users))
    
    for j in range(0, 500001):
        percent_users[j] = num_users[j] / total_u
        #percent_users[j] = num_users[j]
    
#    plt.plot(num_calls, num_users, label= 'prob distribution of frequency of calls')
    plt.plot(fq_calls, percent_users, label= 'pdf fq calls')
        

        
#    plt.yscale('log')
#    plt.xscale('log')
#    plt.xlim(0, 256)
    plt.xlabel('N, fq calls')
    plt.ylabel('P(N)')
    plt.legend()    
    #plt.show()
    figure_name = "/home/sscepano/D4D res/SET3 frequent callers from python/SET3 ONLY FQ distr of fq of calls.png"
    print(figure_name)
    plt.savefig(figure_name, format = "png")        
#    #  avg =  avg / len(usr_group)    
#    # print avg 
    
    return
    

plot_pdf_python_out("/home/sscepano/D4D res/SET3 frequent callers from python/Only_FQ_callers_0.25.tsv")