import sys
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import time
from bSort import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")
fig, axs = plt.subplots(1, 1)

nmax = 15000
kmax = 1

timeIS = [0 for x in range(0, nmax)]
opsIS = timeIS.copy()
timeMS = timeIS.copy()
opsMS = timeIS.copy()

def insertionSortExec(l):
    return [len(l), len(l)-1]

def mergeSortExec(l, k):
    return [k, l[k]]         

def test1(): # timeIS opsIS timeMS opsMS
    l1 = [x for x in range(nmax)]
    print("finised calculating l1")
    for n in range(0, nmax):
        i = l1[0:n]
        rnd.shuffle(i)
        IS = insertionSortExec(i)
        timeIS.append(IS[0])
        opsIS.append(IS[1])

        for k in range(1, kmax+1):
            MS = mergeSortExec(i, k)
            timeMS.append(MS[0])
            opsMS.append(MS[1])

        print("finished calculating {}/{}".format(n, nmax))
        



def test2(): # timeMS opsMS n/k
    l2 = [x for x in range(nmax)]
    rnd.shuffle(l2)
    timeMIS = []
    timeMBS = []
    timeIS = []
    nscale = []
    for n in range(1, nmax, nmax//20):
        i = l2[0:n+1]
        nscale.append(n)
        ri = i.copy()

        si = time.time()
        ri.sort()
        ei = time.time()
        timeIS.append(ei-si)
        
        s1 = time.time()
        r1 = mergeSort(i, insertionSort)
        e1 = time.time()
        timeMIS.append(e1-s1)

        s2 = time.time()
        r2 = mergeSort(i, binarySort)
        e2 = time.time()
        timeMBS.append(e2-s2)

##        print(ri)
##        print(r1)
##        print(r2)
        
        if r1 != ri:
            print("wrong value for 1")
        if r2 != ri:
            print("wrong value for 2")
            
        print("{}/{}".format(n, nmax))

        
    axs.plot(nscale, timeMIS,  label="MIS time")
    axs.plot(nscale, timeMBS, label="MBS time")
    axs.plot(nscale, timeIS, label="Inbuilt")
    ##.set_xlim(0, nmax)
    ##axs.set_ylim(0, 200)
    axs.set_xlabel('sample size')
    axs.set_ylabel('time')               

        
    


test2()
axs.grid(True)
plt.legend(loc='best')
fig.tight_layout()
plt.show()
