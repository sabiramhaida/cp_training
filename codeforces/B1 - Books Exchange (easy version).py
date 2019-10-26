q=int(input())
 
def ruturnn(books,st):
    s=books[st]
    for i in range(len(books)):
        if(s==st+1):
            print(i+1,end="  ")
            break
        else:
            s=books[s-1]
        
for i in range(q):
    n=int(input())
    Books=list(int(i) for i in input().split())
    for i in range (n): 
        ruturnn(Books,i)