#def DFS(tree, visit, ans, node): 
#	res = 0
#	x = 0
#	visit[node] = 1
#	for i in range(len(tree[node])): 
#		if (visit[tree[node][i]] == 0): 
#			x = DFS(tree, visit, ans,tree[node][i]) 
#			if(x % 2): 
#				res += x 
#			else: 
#				ans[0] += 1
#	return res + 1
#
#def maxCut(tree, n): 
#	visit = [0] * (n + 2) 
#	ans = [0] 
#	DFS(tree, visit, ans, 1) 
#	return ans[0]
 
def dfs2(g,s,n):
    parent = [0]*(n+1)
    counts = [1]*(n+1)
    stack = []
 
    stack.append(s)
        
    while stack:
        v = stack[-1]
        empty_s = True
        
        if not parent[v]:
            parent[v] = 1
        
        for node in g[v]:
            if not parent[node]:
                parent[node] = v
                stack.append(node)
                empty_s = False
                
        if empty_s:
            stack.pop()
            counts[parent[v]] += counts[v]
    
    return sum([1 for x in counts[2:] if x % 2 == 0])
 
 
n = int(input())
tree = [[] for i in range(n + 1)]
if(n%2==1):
    for i in range(n-1):
        [u, v]=list(int(node) for node in input().split())
    print(-1)
else:
    for i in range(n-1):
        [u, v]=list(int(node) for node in input().split())
        tree[u].append(v)
        tree[v].append(u)
    print(dfs2(tree,1, n))
