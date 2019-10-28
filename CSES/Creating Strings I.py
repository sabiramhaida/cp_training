from itertools import permutations as perm
string=input()
permut=set(perm(string))
print(len(permut))
permut=list(permut)
permut.sort()
for i in permut:
    s=""
    for k in i:
        s+=k
    print(s)