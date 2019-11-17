input()
A=list(int(i) for i in input().split())
input()
Q=list(int(i) for i in input().split())
piles=[]
i = 1
for wnum in A:
    piles += [i]*wnum
    i += 1
for q in Q:
    print(piles[q-1])