def GCD(a,b):
    if(b==0):
        return a
    return GCD(b,a%b)


T=int(input())
for t in range(T):
    ang=int(input())
    pgdc=GCD(ang,180)
    n=180//pgdc
    i=ang//pgdc
    if(i==n-1):
        n = n*2
    print(n)
    