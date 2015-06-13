#ex1.py
'''Ex1: Infinite Typing Pythons:
Write a program that will randomly generate strings and then check if it
is correct against a set phrase (like Monkeys + Typewrites -> Shakespeare).

Then write a program that will only keep the right letters and randomize the 
remaining ones (a basic 'hill climbing algorithm'. Compare'''
#eventually this was continuously modified to 

import time
import string 
import random
import math

def crudest_pythons(shax):
    char_dict =  dict(enumerate(list(string.lowercase+" ,.?'")))
    tally = 0

    while True:
        gibberish = ''
        while len(gibberish) < len(shax):
            key = random.randint(0,len(char_dict)-1)
            gibberish += char_dict[key]            
        tally +=1

        if gibberish == shax:
            break
 
    return tally

def crude_pythons(shax):
    char_str = string.lowercase + " ,.?'"
    tally = 0
    shax_list = list(shax)
    
    while True:
        gibber_list = [random.choice(char_str) for _ in range(len(shax))]
        if gibber_list == shax_list:
            break
        tally +=1 
    return tally

def smart_pythons(shax):
    char_str = string.lowercase + " ,.?'"
    tally = 0 
    shax_list = list(shax)
    gibber_list = [random.choice(char_str) for _ in range(len(shax))]

    while True:
        if gibber_list == shax_list:
            break  
        for i in range(len(shax)):
            if gibber_list[i] != shax_list[i]:
                gibber_list[i] = random.choice(char_str)
        tally +=1
    return tally

def straight_compare(shax):
    start = time.time()
 
    start = time.time()
    crudest = crudest_pythons(shax)
    lapA = time.time()
    crude = crude_pythons(shax)
    lapB = time.time()
    smart = smart_pythons(shax)
    lapC = time.time()

    return [(crudest,int(lapA-start)) ,(crude,int(lapB-lapA)), (smart, int(lapC-lapB))]

def meanvar(nlist):
    total = 0
    totalsq = 0
    for n in nlist:
        total += n
        totalsq += n*n


    mean = float(total)/len(nlist)
    var = (float(totalsq)/len(nlist)) - (mean**2)
    st_dev = math.sqrt(var)

    return (mean, st_dev)

def stats(shax,sample_size=5 ):
    i = 0 
    crudest, crude, smart = [],[],[]
    cest_time, c_time, s_time = [],[],[]

    while i<sample_size:
        sample = straight_compare(shax)
        crudest.append(sample[0][0])
        crude.append(sample[1][0])
        smart.append(sample[2][0])
        cest_time.append(sample[0][1])
        c_time.append(sample[1][1])
        s_time.append(sample[2][1])
        i+=1


    res = [meanvar(crudest), meanvar(crude), meanvar(smart),
            meanvar(cest_time), meanvar(c_time), meanvar(s_time)]

    print '----- phrase: \'%s\'  :  size : %s  -----' %(shax, sample_size)
    print '''
    NUMBER:     
    Crudest   : %s  ,  (%s)
    Crude     : %s  ,  (%s)
    Smart     : %s  ,  (%s)

    TIME:
    Crudest   : %s  ,  (%s)
    Crude     : %s  ,  (%s)
    Smart     : %s  ,  (%s)
    ''' % (res[0][0],res[0][1],res[1][0],res[1][1],res[2][0],res[2][1],
           res[3][0],res[3][1],res[4][0],res[4][1],res[5][0],res[5][1])
    




if __name__ == '__main__':
    start = time.time()
    shax = raw_input('keep it short>>')
    if not shax:
        shax = "hal"
    print stats(shax, 5)
    print stats(shax, 15)
    print stats(shax, 1000)
