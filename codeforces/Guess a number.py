Q=int(input())
minn=-2*10**9
maxx =2*10**9
d = {">=":"<", ">":"<=", "<":">=", "<=":">"}
for q in range(Q):
	op, x, Answer = input().split()
	x = int(x)
	if Answer == "N": op = d[op]
	if op[0]=="<":
		if op == '<': x -= 1
		maxx = min(maxx, x)
	if '>' in op:
		if op == '>': x += 1
		minn = max(minn, x)

if (minn <= maxx):
    print (minn)
else:
    print("Impossible")