def solve(array,n,s):
    temp=0
    for i in range(n):
        temp=max(temp,array[i])
        if(s[i]=='0' and temp>i+1):
                print("NO")
                return
    print("YES")

n=int(input())
array=list(int(i) for i in input().split())
s=input()+'0'
solve(array,n,s)