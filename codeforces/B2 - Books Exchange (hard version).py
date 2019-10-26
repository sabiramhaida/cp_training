import sys
input=sys.stdin.readline
for i in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    res = [0]*n
    for j in range(n):
        if res[j] == 0:
            tmp = [j]
            con = 1
            ind = a[j]-1
            while ind != j:
                con+=1
                tmp.append(a[ind]-1)
                ind = a[ind] -1
            for _ in tmp:
                res[_] = con
    print(*res)