n=int(input())
s=input()
if(s[::-1][10:].count('8')>(n-11)//2):
    print("YES")
else:
    print("NO")
