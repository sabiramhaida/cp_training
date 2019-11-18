def solve(n,k,A):
    store=0
    for i in range(n):
        prot=store+A[i]
        if(prot<k):
            print("NO",i+1)
            return
        else:
            store=prot-k
    print("YES")

T=int(input())
for t in range(T):
    n,k=list(int(i) for i in input().split())
    A=list(int(i) for i in input().split())
    solve(n,k,A)
    