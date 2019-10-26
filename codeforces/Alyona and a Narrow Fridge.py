L=list(int(i) for i in input().split())
n=L[0]
h=L[1]
A=list(int(i) for i in input().split())
def ispossible(L,h):
    x=0
    for i in range(len(L)-1,-1,-2):
        x+=L[i]
    return x<=h
 
for k in range(n,0,-1):
    x=A[:k+1]
    x.sort()
    if(ispossible(x,h)):
        print(len(x))
        break
    