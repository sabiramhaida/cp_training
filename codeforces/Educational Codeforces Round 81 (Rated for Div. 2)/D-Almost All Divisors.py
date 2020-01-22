def primFactors(Number):
    i = 2
    pF = []
    while i * i <= Number:
        if Number % i == 0:
            pF.append(i)
            pF.append(Number // i)
        i += 1
    return pF
 
def solve():
    n = int(input())
    div = sorted(list(map(int,input().split())))
    x = div[0] * div[-1] 
    div1 = primFactors(div[0])
    div2 = primFactors(div[-1])
    
    if div1 :
        return -1
 
    test = set([div[0], div[-1]] + div2)
    test = test.union(set(div[0] * k for k in div2))
    
    if set(div) == test:
        return x
    return -1
 
q = int(input())
for z in range(q):
    print(solve())