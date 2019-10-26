[hh,mm]=list(int(i) for i in input().split())
 
[H,D,C,N]=list(int(i) for i in input().split())
temp1=0
temp2=0
temp1=H//N
if(H%N!=0):
    temp1+=1
temp1*=C
time=0
if(hh<20):
    time=20-hh
    time*=60
    time-=mm
temp2=time*D+H
H=temp2
temp2=H//N
if(H%N!=0):
    temp2+=1
 
temp2*=C
 
temp2=(0.8*temp2)
print(min(temp1,temp2))
