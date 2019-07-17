from collections import Counter
n= int(input())
numbers = list(map(int,input().split()))
q = int(input())
occurences = Counter(numbers)
for i in range(q):
    x = int(input())
    if occurences[x]:
        print(occurences[x])
    else:
        print("NOT PRESENT")