[N,M]=list(int(i) for i in input().split())
L=[]
rep="YES"
if(M>0):
    L=list(int(i) for i in input().split())
    L=sorted(L)
    if(L[0]==1 or L[M-1]==N):
        rep="NO"
    else:
        for i in range(2,M):
            if(L[i]==L[i-1]+1 and L[i]==L[i-2]+2):
                rep="NO"
                break
print(rep)