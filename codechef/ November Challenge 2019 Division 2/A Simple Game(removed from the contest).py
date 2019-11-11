def SimplGame(M):
    M=sorted(M)[::-1]
    ChefScore=0
    for i in range(0,len(M),2):
        ChefScore+=M[i]
    return ChefScore

T=int(input())
for i in range(T):
    N=int(input())
    M=[]
    score=0
    for j in range(N):
        L=list(int(i) for i in input().split())
        C=L.pop(0)
        if(C%2==0):
            score+=sum(L[:C//2])        
        else:
            M.append(L[C//2])
            score+=sum(L[:C//2])
    print(SimplGame(M)+score)
