T=int(input())
for i in range(T):
    N=int(input())
    L=[0]
    while(len(L)<N):
        if(L[-1] not in L[:len(L)-1]):
            L.append(0)
        else:
            L.append(L[len(L)-2::-1].index(L[-1])+1)
        
    print(L.count(L[N-1]))