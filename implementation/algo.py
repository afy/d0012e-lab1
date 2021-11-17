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

def mergeSort(a, sort, d):
    if len(a) == 1 or d == 0:
        return a
    mid = len(a) // 2
    l = mergeSort(a[mid:], sort, d-1)
    r = mergeSort(a[:mid], sort, d-1)    
    return sort(l + r)  

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
