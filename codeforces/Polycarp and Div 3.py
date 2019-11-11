N=input()
l = len(N)
cuts = 0
TestNum = 0
for i in range(l):
	n = int(N[i])
	TestNum = TestNum + n
	if(n % 3 == 0):
		cuts += 1
		TestNum = 0
	elif TestNum%3 == 0:
		cuts += 1
		TestNum = 0
	elif (TestNum%100)%3 == 0:
		cuts += 1
		TestNum = 0
	else:
		TestNum = TestNum*10
print (cuts)