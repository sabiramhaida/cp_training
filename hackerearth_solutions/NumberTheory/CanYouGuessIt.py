inp=list(int(i) for i in input().split())
A=inp[0]
B=inp[1]
C=inp[2]
M=inp[3]
print (inp)
def ApowerB(A,B,M):
    if(B==0):
        return 1
    else:
        if B%2==0:
            return ApowerB(A*A%M,B//2,M)
        else:
            return ApowerB(A*A%M,(B-1)//2,M)
            
print(((ApowerB(A,B,M))/(C%M))%M)
            