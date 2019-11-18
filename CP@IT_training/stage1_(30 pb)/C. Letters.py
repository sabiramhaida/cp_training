n,M=list(int(i) for i in input().split())
A=[0]+list(int(i) for i in input().split())
q=list(int(i) for i in input().split())
def Ceil_BinarySearch(arr, l, r, x): 
	if x <= arr[l]: 
		return l 
	m = (l + r)//2 
	if arr[m] == x: 
		return m
 
	elif arr[m] < x: 
		if m + 1 <= r and x <= arr[m+1]: 
			return m + 1
		else: 
			return Ceil_BinarySearch(arr, m+1, r, x) 
	else: 
		if m - 1 >= l and x > arr[m-1]: 
			return m 
		else: 
			return Ceil_BinarySearch(arr, l, m - 1, x)

for i in range(1,n+1):
    A[i]+=A[i-1]
print(A)
for i in q:
    d=Ceil_BinarySearch(A,0,n-1,i)
    k=i-A[d-1]
    print(d,k)