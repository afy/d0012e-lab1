import sys
import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import threading
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
matplotlib.use("TkAgg")
fig, axs = plt.subplots(1, 1)

nmax = 10000
kmax = 1

timeIS = [0 for x in range(0, nmax)]
opsIS = timeIS.copy()
timeMS = timeIS.copy()
opsMS = timeIS.copy()

def insertionSortExec(l):
    return [len(l), len(l)-1]

def mergeSortExec(l, k):
    return [k, l[k]]

class MyThread (threading.Thread):
   def __init__(self, l, o, t):
      threading.Thread.__init__(self)
      self.l = l
      self.o = o
      self.t = t 
   def run(self):
        for i in range(0, len(self.l)):
            IS = insertionSortExec(self.l)
            timeIS[i+self.o] = IS[0]
            opsIS[i+self.o] = IS[1]

            MS = mergeSortExec(self.l, 1)
            timeMS[i+self.o] = MS[0]
            opsMS[i+self.o] = MS[1]
        self.t[self.o-1] = 1

        show = True
        for el in self.t:
            if el != 1:
                show = False
        if show:
            axs.plot(timeIS, label="IS time")
            axs.plot(opsIS, label="IS ops")
            axs.plot(timeMS, label="MS time")
            axs.plot(opsMS, label="MS ops")
            axs.set_xlim(0, nmax)
            axs.set_ylim(0, 200)
            axs.set_xlabel('size')
            axs.set_ylabel('sort')               


def test1_t():
    l1 = [x for x in range(nmax)]
    t = []
    print("finised calculating l1")
    for i in range(0, nmax//1000):
        MyThread(l1[0:i], i, t).start()
        t.append(0)

def test1(): # timeIS opsIS timeMS opsMS
    l1 = [x for x in range(nmax)]
    print("finised calculating l1")
    for n in range(0, nmax):
        i = l1[0:nmax]
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
    pass
    


test1()
axs.grid(True)
plt.legend(loc='best')
fig.tight_layout()
plt.show()
