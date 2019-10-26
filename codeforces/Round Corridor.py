[n,m,q]=list(int(i) for i in input().split())
def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)
pgcd=gcd(n,m)
n2=n//pgcd
m2=m//pgcd
 
for i in range(q):
    [s1,s2,e1,e2]=list(int(i) for i in input().split())
    temp1=0
    temp2=0
    s2-=1
    e2-=1
    if(s1==1):
        temp1=s2//n2
    else:
        temp1=s2//m2
    if(e1==1):
        temp2=e2//n2
    else:
        temp2=e2//m2
        
    if(temp1==temp2):
        print("YES")
    else:
        print("NO")