n=int(input())
for i in range(n):
    s=input()
    numberOfGoodSub=0
    for  r in range(1,25):
        zeros=0
        for l in range(len(s)-r+1):
            if(s[l]=='0'):
                zeros+=1
                continue
            x=int(s[l:l+r],2)
            if((x-r)<=zeros):
                numberOfGoodSub+=1
            zeros=0
    print(numberOfGoodSub)
