import sys
# Write your code here
def base_9( num):
    if(num < 9):
        return num
    else:
        return num%9 + 10*base_9(num//9)
while True:
    number= sys.stdin.readline()
    if number == '':
        break
    print(base_9(int(number)))