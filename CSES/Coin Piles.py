t=int(input())
for i in range(t):    
    [a,b]=list(int(i) for i in input().split())
    if((a+b)%3==0 and 2*min(a,b)>=max(a,b)):
        print("YES")
    else:
        print("NO")
