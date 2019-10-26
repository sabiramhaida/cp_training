q=int(input())
 
def solve(n):
    if n == 0:
        return False
    while n:
        n, r = divmod(n, 3)
        if(r==2):
            return False
    return True
 
for i in range(q):
    n=int(input())
    m=n
    while(True):
        if(solve(m)):
            print(m)
            break
        m=m+1