T=int(input())
for k in range(T):
    N=int(input())
    s=int(input(),2)
    for i in range(N-1):
        s^=int(input(),2)
    num='{0:b}'.format(s)
    print(num.count('1'))
        
    