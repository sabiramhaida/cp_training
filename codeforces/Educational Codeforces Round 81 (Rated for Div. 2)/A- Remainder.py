[n, x, y] = list(map(int, input().split()))
Bnum = input()
Bnum = Bnum[-x:]
res = 0
for k in range(x):
    f = x-y-1
    if (Bnum[k] == '0' and k == f):
        res += 1
    elif (Bnum[k] == '1' and k != f) :
        res += 1
print(res)