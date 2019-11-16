T=int(input())
for t in range(T):
    S=input()
    lenght=len(S)
    if(lenght>10):
        print(S[0]+str(lenght-2)+S[lenght-1])
    else:
        print(S)