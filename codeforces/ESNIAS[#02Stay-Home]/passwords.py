n,k = list(map(int,input().split()))
passwds = list()
for i in range(n):
    p = str(input())
    lenght = len(p)
    passwds.append(lenght)

rightPass = input()
rightPasslen = len(rightPass)

passwds = sorted(passwds)
A = 0
B = 0
for i in range(n):
    if(passwds[i]>rightPasslen):
        break
    elif(rightPasslen==passwds[i]):
        B+=1
    else:
        A+=1
B=B+A
WorstCase = ((B-1)//k)*5 + B 
BestCase = (A//k)*5 + A + 1
print(BestCase, WorstCase)