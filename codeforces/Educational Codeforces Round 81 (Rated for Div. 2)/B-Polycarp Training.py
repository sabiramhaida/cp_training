NumberOfContests=int(input())
contests = sorted(list(map(int,input().split())))
k=0
for p in contests:
   
    if( p > k):
        k+=1
print(k)
    