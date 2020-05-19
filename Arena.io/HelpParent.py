for t in range(int(input())):
    N, Word = list(input().split())
    N = int(N)
    print(t+1,Word[:N-1]+Word[N:])

