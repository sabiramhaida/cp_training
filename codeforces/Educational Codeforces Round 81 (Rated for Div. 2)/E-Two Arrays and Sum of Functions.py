n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(n):
	A[i] = A[i] * (i+1) * (n - i)  #le res de la somme de somme de i (nbr d'occurence de ai dans la solution !)
A=sorted(A)
B=sorted(B)[::-1]
res = 0
 
for i in range(n):
	res += (A[i] * B[i]% 998244353) % 998244353 
print(res%998244353)  