#ex2.py 
'''Just a simple implementation of two searching/matching algoriths. 
One must be O(n) and one O(n^2).'''
import time
import random

def order_n(inlist):
    store = inlist[0]

    for i in inlist:
        if store > i:
            store = i

    return store

def order_n_sq(inlist):
    store = inlist[0]
    switch = 0

    for i in inlist:
        switch = 0
        for j in inlist:
            if i>j:
                switch+=1
        if switch == 0:
            store = i


                
    return store

def random_list_gen(length= 10000):
    
    return [random.randint(0,10000000) for _ in range(length)]


if __name__ == '__main__':
    no = raw_input('>>>')
    if not no:
        no = 10000
    to_be_sorted = random_list_gen(int(no))

    start = time.time()
    lowestN = order_n(to_be_sorted)
    lap = time.time()
    lowestN2 = order_n_sq(to_be_sorted)
    end = time.time()

    print '--------  O(n^2) for len(%s) found %s in %ss --------' %\
    (len(to_be_sorted), lowestN2, end-lap)
    print '--------  O(n)   for len(%s) found %s in %ss --------' %\
    (len(to_be_sorted), lowestN, lap-start)






