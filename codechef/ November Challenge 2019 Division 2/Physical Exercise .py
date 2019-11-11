import numpy as np
from scipy.spatial import distance
from math import sqrt
T=int(input())

def points2D(array):
    s=[]
    while(array!=[]):
        s.append((array.pop(0),array.pop(0)))
    return s

def Dist(c1,c2):
    global x,y,c3,mindist
    for n in c1:
        dn = sqrt((x-n[0])**2 + (y-n[1])**2)
        if dn > mindist:
            continue
        for m in c2:
            dm = sqrt((m[0]-n[0])**2 + (m[1]-n[1])**2)
            if dm+dn > mindist:
                continue
            for k in c3:
                dk = sqrt((m[0]-k[0])**2 + (m[1]-k[1])**2)
                mindist = min(mindist, dn + dm + dk)

for i in range(T):
    (x, y) = tuple(int(i) for i in input().split())
    [N, M, K] = list(int(i) for i in input().split())
    c1= points2D(list(int(i) for i in input().split()))
    c2= points2D(list(int(i) for i in input().split()))
    c3= points2D(list(int(i) for i in input().split()))
    mindist=10000000000000000
    Dist(c1,c2)
    Dist(c2,c1)
    print(mindist)