for _ in range(int(input())):
    a,b=list(int(i) for i in input().split())
    vol=abs(b-a)
    c=0
    print(vol//5+(vol%5)//2+(vol%5)%2)