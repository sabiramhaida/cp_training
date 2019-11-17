from itertools import groupby
from re import search
#using regular expression ...
L="h+.*e+.*l+.*l+.*o+"
S=input()
if(search(L,S)):
    print("YES")
else:
    print("NO")

