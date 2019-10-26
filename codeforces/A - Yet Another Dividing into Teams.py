q=int(input())
for i in range(q):
    n=int(input())
    teams=1
    students=list(int(i) for i in input().split())
    students=sorted(students)
    
    for i in range(n-1):
        if((students[i+1]-students[i])==1):
            teams+=1
            
    if(teams>2):
        print(2)
    else:
        print(1)