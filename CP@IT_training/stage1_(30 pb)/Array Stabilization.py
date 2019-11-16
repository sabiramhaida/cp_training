N=int(input())
L=list(int(i) for i in input().split())
L.sort()
print(min(L[N-1]-L[1],L[N-2]-L[0]))