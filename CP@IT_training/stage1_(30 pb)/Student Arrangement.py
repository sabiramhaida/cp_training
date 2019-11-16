n, m, k = list(int(i) for i in input().split())
available = {}
seats = [0] * m
notPreffered = max(0, n - m * k)
choices = list(int(i) for i in input().strip().split())
choices=choices[:min(n, m * k)]
for P_row in choices:
    P_row -= 1
    if seats[P_row] < k:
        seats[P_row] += 1
    else:
        notPreffered += 1
        NextAvailabeRow = available[P_row] if P_row in available else P_row
        while seats[NextAvailabeRow] == k:
            NextAvailabeRow = (NextAvailabeRow + 1) % m
        seats[NextAvailabeRow] += 1
        available[P_row] = NextAvailabeRow

print(notPreffered)