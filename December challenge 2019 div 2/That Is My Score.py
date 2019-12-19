for t in range(int(input())):
    scores = [0,0,0,0,0,0,0,0]
    n=int(input())
    for i in range(n):
        p, sc = list(map(int,input().split()))
        if(p <= 8):
            scores[p-1] = max(scores [p-1],sc)
    print(sum(scores))