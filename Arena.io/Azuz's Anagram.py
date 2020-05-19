for _ in range(int(input())):
    W1, W2 = input().split()
    len1, len2 = len(W1), len(W2)
    if(len1 != len2):
        print('Azuz is not my leader')
    elif(len1 < 4 and W1 != W2):
        print('Azuz is not my leader')
    else:
        if(W1[0] != W2[0] or W1[len1 - 1] != W2[len2 - 1]):
            print('Azuz is not my leader')
        elif(sorted(W1)==sorted(W2)):
            print('Awesome anagram')
        else:
            print('Azuz is not my leader')
