for l in range(int(input())):  
    n=int(input())
    arr=sorted(list(map(int,input().split())),reverse=True)
    arr.append(0)
 
    k=0
    while arr[k]>k:
        k+=1
    print(k)