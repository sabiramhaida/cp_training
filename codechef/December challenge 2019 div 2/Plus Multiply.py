from collections import Counter 
for t in range(int(input())):
    n=int(input())
    pairs = 0
    num = list(map(int,input().split()))
    d = Counter(num)
    if(d[0] >= 2):
        pairs += (d[0]*(d[0]-1))//2
    if(d[2] >= 2):
        pairs += (d[2]*(d[2]-1))//2
    print (pairs)