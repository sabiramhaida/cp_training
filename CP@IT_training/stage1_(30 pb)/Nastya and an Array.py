N=int(input())
c=0
for i in set(input().split()):
    if i!='0':
        c+=1
print(c)