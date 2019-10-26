[n,k]=list(int(i) for i in input().split())

shortenedMod =k-1

while(n%shortenedMod!=0):
    shortenedMod=shortenedMod-1

x=(n//shortenedMod)*k+shortenedMod

print(x)