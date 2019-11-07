[n,k]=list(int(i) for i in input().split())
L=list(int(i) for i in input().split())
Numodd,Numeven=0,0
temp=len(L)
M=[]
NumberOfCut=0
test = 0

for j in range(temp):
    if(L[j]%2==0):
        Numeven+=1
    else:
        Numodd+=1
    if(j!=temp-1 and  Numeven==Numodd):
        M.append(abs(L[j+1]-L[j]))
M=sorted(M)
for elt in M:
    k-=elt
    NumberOfCut+=1
    if(k<0):
        test = 1
        break
    if(k==0):
        break
    
print(NumberOfCut-test)