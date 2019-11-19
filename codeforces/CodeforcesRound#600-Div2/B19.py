for _ in range(int(input())):
    n,m=list(map(int,input().split()))
    arr=list(int(i) for i in input().split())
    d=((i,c) for c,i in enumerate(arr))
    d=sorted(d)
    m1=d[0]
    m2=d[1]
    cost=0
    pairs=[]
    if(n>m or n==2):
        print(-1)
    elif(n==m):
        print(2*sum(arr))
        for i in range(n-1):
            print(d[i][1]+1,d[i+1][1]+1)
        print(d[n-1][1]+1,d[0][1]+1)
    else:
        M=m
        for i in range(2,n):
            cost+=m1[0]+m2[0]+2*d[i][0]
            M-=2
        cost+=(m1[0]+m2[0])*M
        print(cost)
        for i in range(2,n):
            print(m1[1]+1,d[i][1]+1)
            print(m2[1]+1,d[i][1]+1)
        for i in range(M):
            print(m1[1]+1,m2[1]+1)

            
        

