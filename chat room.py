from itertools import groupby
from re import search
L="h+.*e+.*l+.*l+.*o+"
S=input()
if(search(L,S)):
    print("YES")
else:
    print("NO")
"""
String=list(i for i in input())
a=[(i,len([*j])) for i,j in groupby(String)]
for i in range(4,len(a)):
    if(a[i][0]=='o' and (a[i-1][0]=='l' and a[i-1][1]>=2) and a[i-2][0]=='e' and a[i-3][0]=='h'):
        print("YES")
        exit(0)
print("NO")
"""