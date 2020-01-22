n = int(input())
s = input()
goodStr = ''
for character in s:
    if( len(goodStr)%2==0  or  character != goodStr[-1]):
        goodStr+=character
 
if(len(goodStr)%2):
    goodStr = goodStr[:-1]
    
print(n-len(goodStr))
print(goodStr)