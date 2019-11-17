N,K=list(int(i) for i in input().split())
freeTime=240-K
while(N>=0):
    requiredTime=5*(N*(N+1)//2)
    if(requiredTime<=freeTime):
        print(N)
        exit(0)
    N-=1
    