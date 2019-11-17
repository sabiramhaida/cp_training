from itertools import groupby
n=int(input())
arr=input().split()
a=[len([*j]) for i,j in groupby(arr)]
left=a[:n-1]
right=a[1:]
print(2*max(map(min,zip(left,right))))
 
"""
#without using groupby and zip ... 
n = int(input())
t = [int(i) for i in input().split()]
last_count = 1
cur_count = 1
result = 0
for i in range(n-1):
    if t[i] == t[i+1]:
        cur_count += 1
    else:
        result = max(min(last_count, cur_count), result)
        last = cur_count
        count = 1
result = max(min(last, count), result)
print(result*2)

"""