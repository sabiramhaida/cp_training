def solve (A,N):
	out_=0
	num=2**(N-1)
	for i in range(N):
		if (A[i]>=num):
			out_+= A[i]
	return out_%(10**9+7)

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    out_ = solve(A,N)
    print (out_)