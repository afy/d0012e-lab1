import random as rnd
import math
import time


def binarySearch(e, a, l, h):
    m = l + (h - l) // 2
    #print("{} {} {} {} {}".format(e, a, l, h, m))
    if h < l:
        return m + 1
    if a[m] == e:
        return m
    elif a[m] > e: # stega ner 
        return binarySearch(e, a, l , m - 1)
    else: # stega upp
        return binarySearch(e, a, m + 1, h)


def binarySort(a):
    na = [a[0]]
    for i in range(1, len(a)-1):
        e = a[i]
        ni = binarySearch(e, na, 0, len(na)-1)
        na = na[:ni] + [e] + na[ni:]
    return na

def insertionSort(arr):
    for i in range(1, len(arr)):  
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    return arr

def mergeSort(a, sort):
    if len(a) == 1:
        return a
    mid = len(a) // 2
    l = sort(mergeSort(a[mid:], sort))
    r = sort(mergeSort(a[:mid], sort))    
    return sort(l + r)
        

l = [rnd.randint(0, 99) for x in range(0,10000)]
print("=")
s1 = time.time()
r1 = mergeSort(l, insertionSort)
e1 = time.time()
print("==")
s2 = time.time()
r2 = insertionSort(l)
e2 = time.time()
print("===")
s3 = time.time()
r3 = mergeSort(l, binarySort)
e3 = time.time()
print("====")
s4 = time.time()
r4 = binarySort(l)
e4 = time.time()
print("M(I): {}  I: {}  M(B): {}  B: {}"
      .format(e1-s1, e2-s2, e3-s3, e4-s4))
