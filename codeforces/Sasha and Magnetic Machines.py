N=int(input())
Machines=list(int(i) for i in input().split())
Machines.sort()
minNumber=Machines[0]
Maxinfluence=0
sum=Machines[0]
for i in range(1,N):
    curr_num=Machines[i]
    sum+=curr_num
    summ=curr_num+minNumber
    for j in range(2,curr_num+1):
        if(curr_num%j==0):
            test=(curr_num//j)+(minNumber*j)
            cur_influence=summ-test
            if(cur_influence>Maxinfluence):
                Maxinfluence=cur_influence
print(sum-Maxinfluence)
                