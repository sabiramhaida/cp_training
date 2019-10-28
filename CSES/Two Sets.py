n=int(input())
arraySum=sum([i for i in range(1,n+1)])
possiblity=(arraySum%2==0)
if(possiblity):
    print("YES")
else:
    print("NO")
S=set()
N=n
N_S1=0
n1=arraySum//2
while(n1>0):
    if(n1>n):
        S.add(n)
        N_S1+=1
        n1-=n
        n-=1
    else:
        S.add(n1)
        N_S1+=1
        break
print(len(S))
for i in S:
    print(i,end=" ")
print()
print(N-len(S))
for i in range(1,n+1):
    if i not in S:
        print(i,end=" ")
    