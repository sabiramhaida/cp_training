import math
n=int(input())
S=list(int(i) for i in input().split())
for i in range(1,n-1):
    S[i+1]+=S[i]
for i in range(int(input())):
    [left,right]=list(int(i) for i in input().split())
    print((S[right]-S[left-1])//2)
        
            
        
            
        
        