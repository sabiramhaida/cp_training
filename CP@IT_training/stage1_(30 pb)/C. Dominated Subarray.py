for _ in range(int(input())):
    mindist=1000001
    n=int(input())
    arr=list(map(int,input().split()))
    arr=list((c,i) for i,c in enumerate(arr))
    arr=sorted(arr)
    if(n<2):
        print(-1)
        continue
    for i in range(n-1):
        if(arr[i][0]==arr[i+1][0]):
            mindist=min(mindist,arr[i+1][1]-arr[i][1]+1)
    if(mindist<1000000):
        print(mindist)
    else:
        print(-1)
        