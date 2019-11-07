N=int(input())
first=[]
last=[]
for name in range(N):
    [a,b]=list(i for i in input().split())
    first.append(a)
    last.append(b)
    if (a>b):
        last[name],first[name]=first[name],last[name]
temp=""
p=list(int(i) for i in input().split())
rep="YES"
for i in p:
    if(first[i-1]>temp):
        temp=first[i-1]
    else:
        if(last[i-1]>temp):
            temp=last[i-1]
        else:
            rep="NO"
            break
print(rep)