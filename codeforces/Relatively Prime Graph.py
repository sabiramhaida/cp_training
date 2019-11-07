def GCD(a,b):
    if(b==0):
        return a
    return GCD(b,a%b)

[n,m] = list(int(i) for i in input().split())
edges=[]
for i in range(n):
    for j in range(i+1,n):
        if(len(edges)==m):
            break
        if(GCD(i+1,j+1)==1):
            edges.append([i+1,j+1])
if(m<n-1):
    print("Impossible")
else:
    if(len(edges)!=m):
        print("Impossible")
    else:
        print("Possible")
        for k in range(m):
            print(edges[k][0]," ",edges[k][1])
        