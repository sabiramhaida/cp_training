n=int(input())
array=list(int(i) for i in input().split())
turns=0
for i in range(n-1):
    if(array[i+1]<array[i]):
        turns+=array[i]-array[i+1]
        array[i+1]=array[i]
print(turns)
    