from collections import Counter
import operator

def palindrome(s,d):
    pal=""
    alpha=sorted(d.items(), key=lambda kv: kv[1])
    f=-1
    for i in alpha:
        if(i[1]%2==0):
            pal+=(i[0]*(i[1]//2))
        else:
            f=alpha.index(i)
    if(f!=-1):
            pal+=alpha[f][0]*alpha[f][1]+pal[::-1]
    else:
            pal=pal[::-1]+pal
    return pal
s=input()
d=list(Counter(s).values())
flag=0
possible=True
for i in d:
    if(i%2!=0):
        flag+=1
    if(flag>=2):
        possible=False
        break
if(not possible):
    print("NO SOLUTION")
else:
    print(palindrome(s,Counter(s)))
    