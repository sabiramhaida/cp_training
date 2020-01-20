from math import sqrt
N=int(input())
a=int(sqrt(N))
b=0
def GCD(a,b): 
    if(b==0): 
        return a 
    else: 
        return GCD(b,a%b)
    
while(True):
    b=N//a
    if(((N%a==0 and a * a !=N) or a==1) and GCD(a,b)==1):
        break
    else:
        a-=1
print(a,b)