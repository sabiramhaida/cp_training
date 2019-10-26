L=list(int(i) for i in input().split())
n=L[0]
m=L[1]
Ma=[[0 for i in range(n)] for  i in range(m)]
for i in range(n):
    mark=input()
    mark=list(mark)
    for j in range(len(mark)):
        Ma[j][i]=int(mark[j])
student=0
c=0
for i in range(n):
    for j in range(m):
        if(max(Ma[j])== Ma[j][i]):
            c+=1
            break
        else:
            pass
print(c)