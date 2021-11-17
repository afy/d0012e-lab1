import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import time
from algo import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")
fig, axs = plt.subplots(1, 1)

nmax = 15000

def test1(): 
    l1 = [x for x in range(nmax)]
    rnd.shuffle(l1)
    timeMIS = []
    timeMBS = []
    timeIS = []
    nscale = []
    for n in range(1, nmax, nmax//20):
        i = l1[0:n+1]
        nscale.append(n)
        
        ri = i.copy()
        si = time.time()
        ri.sort()
        ei = time.time()
        timeIS.append(ei-si)
        
        s1 = time.time()
        r1 = mergeSort(i, insertionSort, 99999)
        e1 = time.time()
        timeMIS.append(e1-s1)
        
        s2 = time.time()
        r2 = mergeSort(i, binarySort, 99999)
        e2 = time.time()
        timeMBS.append(e2-s2)
        
        if r1 != ri: print("wrong value for 1")
        if r2 != ri: print("wrong value for 2")
            
        print("{}/{}".format(n, nmax))
        
    axs.plot(nscale, timeMIS,  label="MIS time")
    axs.plot(nscale, timeMBS, label="MBS time")
    axs.plot(nscale, timeIS, label="Inbuilt")


def test2():
    l2 = [x for x in range(nmax)]
    rnd.shuffle(l2)
    steps = 8
    times = []
    titles = [2**(it) for it in range(steps)]
    for t in range(steps): times.append([])
    nscale = []
    for n in range(1, nmax, nmax//7):
        i = l2[0:n+1]
        nscale.append(n)      
        for it in range(steps):
            s = time.time()
            mergeSort(i, binarySort, titles[it])
            e = time.time()
            times[it].append(e-s)
    
        print("{}/{}".format(n, nmax))

    for j in range(steps):
         axs.plot(nscale, times[j], label="k="+str(nmax//titles[j]))
     
    
def test3():
    ls = [x for x in range(nmax)]
    lns = [x for x in range(nmax)]
    rnd.shuffle(lns)
    
    mid = nmax//2
    lps1 = [x for x in range(mid)]
    lps2 = [x for x in range(mid, nmax)]
    rnd.shuffle(lps1)
    lps = lps1 + lps2
    
    timels = []
    timelps = []
    timelns = []
    nscale = []
    for n in range(1, nmax, nmax//10):
        nscale.append(n)

        s1 = time.time()
        mergeSort(ls[0:n+1], binarySort, 999999)
        e1 = time.time()
        timels.append(e1 - s1)

        s2 = time.time()
        mergeSort(lps[0:n+1], binarySort, 999999)
        e2 = time.time()
        timelps.append(e2 - s2)

        s3 = time.time()
        mergeSort(lns[0:n+1], binarySort, 999999)
        e3 = time.time()
        timelns.append(e3 - s3)
        
        print("{}/{}".format(n, nmax))
        
    axs.plot(nscale, timels,  label="Fully sorted")
    axs.plot(nscale, timelps, label="Partially sorted")
    axs.plot(nscale, timelns, label="Not sorted (random)")


test1()
#test2()
#test3()
axs.set_xlabel('sample size')
axs.set_ylabel('time')   
axs.grid(True)
plt.legend(loc='best')
fig.tight_layout()
plt.show()
