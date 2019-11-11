 
[n, m]= list(int(i) for i in input().split())
G = dict()
for i in range(1, n+1):
	G[i] = set()
 
for k in range(m):
	[u,v]=list(int(i) for i in input().split())
	G[u].add(v)
 
c = 0
for i in range(1, n+1):
	visited = {}
	for s in G[i]:
		Adj = G[s]
		for n in Adj:
			if n != i:
				if n not in visited:
					visited[n] = 1
				else:
					visited[n] += 1
	for x in visited.values():
           c+=(x*(x-1))//2
print(c)