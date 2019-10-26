n=int(input())
s=input()
rightletter=s[0]
leftletter=s[-1]
 
right_s=0
 
for i in range(n):
    if(s[i]==rightletter):
        right_s+=1
    else:
        break
    
left_s=0
for i in range(n-1,0,-1):
    if(s[i]==leftletter):
        left_s+=1
    else:
        break
 
if(rightletter!=leftletter):
    print((right_s+left_s+1)%998244353)
else:
    print(((right_s+1)*(left_s+1))%998244353)