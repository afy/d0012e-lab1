import random as rnd
import math
import time

def binarySearch(e, a, l, h):
    m = l + (h - l) // 2
    if h < l:
        return m + 1
    if a[m] == e:
        return m
    elif a[m] > e:
        return binarySearch(e, a, l , m - 1)
    else:
        return binarySearch(e, a, m + 1, h)

def binarySort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        if temp < a[j]:
            ni = binarySearch(temp, a, 0, j)
            del a[i]
            a = a[:ni] + [temp] + a[ni:]
    return a

def insertionSort(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i-1
        while j >= 0 and a[j] > temp:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1
    return a

def mergeSort(a, sort, k):
    if len(a) <= k:
        return sort(a)
    
    mid = len(a) // 2
    l = mergeSort(a[mid:], sort, k)
    r = mergeSort(a[:mid], sort, k)

    ret = []
    while len(l) > 0 and len(r) > 0:
        if l[0] > r[0] or l[0] == r[0]:
            ret.append(r[0])
            del r[0]
        elif r[0] > l[0]:
            ret.append(l[0])
            del l[0]
            
    for el in l:
        ret.append(el)
    for er in r:
        ret.append(er)
             
    return ret

##mergeSort([rnd.randint(0,999) for x in range(0, rnd.randint(0,500000))], binarySort, 1000)
##print("done")

##while 1:
##    l = [rnd.randint(0,999) for x in range(0, rnd.randint(0,5000))]
##    r = l.copy()
##    r.sort()
##    if mergeSort(l, binarySort, 2) != r: print("u fucked up son")
##
##    print("ok")

##while 1:
##    l = [rnd.randint(0,999) for x in range(0, rnd.randint(0,5000))]
##    r = l.copy()
##    r.sort()
##    r1 = insertionSort(l)
##    r2 = binarySort(l)
##
##    if r1 != r: print("r1")
##    if r2 != r: print("r2")
##
##    print("ok")
##l = [rnd.randint(0, 99) for x in range(0,5)]
##print("<==" + str(l))
##print("==>", binarySort(l))
##ss = time.time()
##x = mergeSort(l, binarySort, 999)
##ee = time.time()
#print("==> {}".format(mergeSort(l, binarySort, 2)))
##print("=")
##s1 = time.time()
##r1 = mergeSort(l, insertionSort)
##e1 = time.time()
##print("==")
##s2 = time.time()
##r2 = insertionSort(l)
##e2 = time.time()
##print("==>" + str(r2))
##print(e2 - s2)
##print("===")
##s3 = time.time()
##r3 = mergeSort(l, binarySort, 999999)
##e3 = time.time()
##print("==>" + str(r3))
##print("====")
##s4 = time.time()
##r4 = binarySort(l)
##e4 = time.time()
##print("{}: {}".format(e3-s3, r3))
##print("M(I): {}  I: {}  M(B): {}  B: {}"
##      .format(e1-s1, e2-s2, e3-s3, e4-s4))
