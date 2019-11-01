[n, m, k] = list(int(i) for i in input().split())
a = sorted(list(int(i) for i in input().split()))
b = sorted(list(int(i) for i in input().split()))

i, j, comp =0, 0, 0
while(i<n and j <m):
    if(a[i] - k > b[j]):
        j+=1
    elif(a[i] + k < b[j]):
        i+=1
    else:
        i+=1
        j+=1
        comp+=1

print(comp)