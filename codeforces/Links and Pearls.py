from collections import Counter 
s=str(input())
d=Counter(s)
if(d['-']==0 or d['o']==0):
    print("YES")
else:
    if(d['-']%d['o']==0):
        print("YES")
    else:
        print("NO")