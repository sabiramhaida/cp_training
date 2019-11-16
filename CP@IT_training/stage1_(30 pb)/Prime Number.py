def SieveEAlgo(n):   
	PrimeNList = [True for i in range(n+1)] 
	p = 2
	while (p * p <= n): 
		if (PrimeNList[p] == True): 
			for i in range(p * p, n+1, p): 
				PrimeNList[i] = False
		p += 1
	for p in range(2, n): 
		if PrimeNList[p]: 
			print(p,end=" ")
N=int(input())

SieveEAlgo(N)