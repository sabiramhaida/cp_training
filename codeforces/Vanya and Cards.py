L=list(int(i) for i in input().split())
n=L[0]
x=L[1]
L=L=list(int(i) for i in input().split())
c=0
curr_sum = abs((sum(L)))
while(curr_sum>0):
    curr_sum-=min(curr_sum,x)
    c+=1
print(c)