N=int(input())
arr=list(int(i) for i in input().split())
d=((i,c) for c,i in enumerate(arr))
d=sorted(d)
for elt in d:
    print(elt[1],end=" ")