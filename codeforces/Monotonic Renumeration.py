mod=998244353
n = int(input())
a = list(map(int, input().split()))
d = dict()

for i in range(n):
    if a[i] not in d:
        d[a[i]] = [i, i]
    else:
        d[a[i]][1] = i
curent_grp = 0

result = 0

for i in range(n):
    if d[a[i]][1] > curent_grp:
        curent_grp = d[a[i]][1]
    if curent_grp == i:
        result += 1
result-=1
result=pow(2, result,mod)
print(result)