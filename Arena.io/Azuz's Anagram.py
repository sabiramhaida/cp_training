def SubsetSumOf(set, i,K, nbr): 
	n = len(set)
	if (i == n): 
		if (K == 0): 
			nbr += 1
		return nbr
	nbr = SubsetSumOf(set, i+1, K - set[i], nbr) 
	nbr = SubsetSumOf(set, i+1, K, nbr) 
	return nbr 

N, K = list(map(int, input().split()))
set = list(map(int, input().split()))

print(SubsetSumOf(set,0,K,0))