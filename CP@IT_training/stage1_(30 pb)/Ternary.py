def turnary(n):
    if(n==0):
        return 0
    s=''
    while(n):
        n,r=divmod(n,3)
        s+=str(r)
    return(s[::-1])
n=0
while(n!=-1):
    n=int(input())
    print(turnary(n))