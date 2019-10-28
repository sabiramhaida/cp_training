n=int(input())
if(2<=n<=3):
    print("NO SOLUTION")
else:
    for i in range(2,n+1,2):
        print(i,end=" ")
    for i in range(1,n+1,2):
        print(i,end=" ")