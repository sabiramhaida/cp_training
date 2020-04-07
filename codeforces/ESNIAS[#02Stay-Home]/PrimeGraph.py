
def GCD(a,b):
    if(b==0):
        return a
    return GCD(b,a%b)

def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True

n=int(input())
edges=list()
NombreOfEdges = n
firstNoeud = 1
secondNoeud = NombreOfEdges//2 + 1

while(isPrime(NombreOfEdges)!=True):
    edges.append((firstNoeud,secondNoeud))
    firstNoeud+=1
    secondNoeud+=1
    NombreOfEdges+=1

print(NombreOfEdges)
print(n,1)
for i in range(1,n):
    print(i,i+1)

for edge in edges:
    print(edge[0],edge[1])