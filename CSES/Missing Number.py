n=int(input())
L=list(int(i) for i in input().split())
L=sorted(L)
smallthenN=0
for i in range(n-1):
    if(L[i]!=i+1):
        print(i+1)
        smallthenN=1
        break
if(smallthenN==0):
    print(n)