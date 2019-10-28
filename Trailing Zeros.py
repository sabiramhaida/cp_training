n=int(input())
k=5
s=0
while(k<=n):
    s+=n//k
    k*=5
print(s)