import re
s=str(input())
heavy=0
res=0
for i in range(4,len(s)):
    if(s[i]=='l'):
        if(s[i-4]=="m" and s[i-3]=="e" and s[i-2]=="t" and s[i-1]=="a"):
            res+=heavy
    else:
        if(s[i-4]=="h" and s[i-3]=="e" and s[i-2]=="a" and s[i-1]=="v" and s[i]=="y"):
            heavy+=1
print(res)