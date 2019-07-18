
n = int(input())
called = list(map(int,input().split()))
ideal = list(map(int,input().split())) 
i=0
Time=0
while(i!=n):  # we can test all possible position in n-1 iteration !! 
    if (called[0] == ideal[0]):
        Time+=1
        x=called.pop(0)
        y=ideal.pop(0)
        i+=1
    else:
        elt=called.pop(0)
        cal.append(elt)
        Time+=1
print(Time)