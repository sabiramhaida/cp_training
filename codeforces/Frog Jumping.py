n= int(input())
for i in range(n):
    L=list( int(i) for i in input().split())
    a=L[0]
    b=L[1]
    k=L[2]
    if(k%2==0):
        print((((k//2))*a)-(k//2)*b)
    else:
        print((((k//2)+1)*a)-(k-1-k//2)*b)