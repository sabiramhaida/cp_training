def inn(string, digits):
    for i in string:
        if (i not in digits):
            return False
    return True
c= 0
X, A, B = list(map(int,input().split()))
digits  = str(input())

for i in range(0,B+1,X):
    if(i>=A and inn(str(i),digits)):
        c+=1
print(c)

