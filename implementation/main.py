import sys
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")
fig, axs = plt.subplots(1, 1)

nmax = 10000
kmax = 1

timeIS = []
opsIS = []
timeMS = []
opsMS = []

def insertionSortExec(l):
    return [len(l), len(l)-1]

def mergeSortExec(l, k):
    return [k, l[k]] 


def test1(): # timeIS opsIS timeMS opsMS
    for n in range(0, nmax):
        i = [rnd.randint(0, 9) for x in range(n)]
        IS = insertionSortExec(i)
        timeIS.append(IS[0])
        opsIS.append(IS[1])

        for k in range(1, kmax+1):
            MS = mergeSortExec(i, k)
            timeMS.append(MS[0])
            opsMS.append(MS[1])

        print("finished calculating {}/{}".format(n, nmax))
        
    axs.plot(timeIS, label="IS time")
    axs.plot(opsIS, label="IS ops")
    axs.plot(timeMS, label="MS time")
    axs.plot(opsMS, label="MS ops")
    axs.set_xlim(0, nmax)
    axs.set_ylim(0, 200)
    axs.set_xlabel('size')
    axs.set_ylabel('sort')


def test2(): # timeMS opsMS n/k
    pass
    


test1()
axs.grid(True)
plt.legend(loc='best')
fig.tight_layout()
plt.show()
