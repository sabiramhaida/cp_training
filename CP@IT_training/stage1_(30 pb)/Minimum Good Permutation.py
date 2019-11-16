T=int(input())
for t in range(T):
    N=int(input())
    for i in range(N-2):
        if(i%2==0):
            print((i+2),end=" ")
        else:
            print(i,end=" ")   
    if(N%2==0):
        print(str(N)+" "+str(N-1))
    else:
        print(str(N)+" "+str(N-2))