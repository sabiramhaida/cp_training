def solve(a,first,last):   
    max_so_far = 0
    meh = 0
    for i in range(first, last):
        meh = meh + a[i]
        if (max_so_far < meh): 
            max_so_far = meh
            
        if meh < 0: 
            meh = 0
    return max_so_far 
 
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    if(solve(arr,1,n) < sum(arr) and solve(arr,0,n-1) < sum(arr)):
        print('YES')
    else:
        print('NO')