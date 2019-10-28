t= int(input())

def solve(x,y):
    a = max(x, y) 
    b = min(x, y) 
    s = (a - 1)* (a-1)
    if (a == b):
         s += a 
    elif (a % 2) :
      if (x == a):
           s+= a * 2 - y 
      else:
          s += x 
    else :
      if (y == a):
           s += a * 2 - x 
      else:
        s += y 
    return s
    

for i in range(t):
    [y,x]=list(int(i) for i in input().split())
    print(solve(x,y))
    
