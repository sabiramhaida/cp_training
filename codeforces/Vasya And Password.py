
    
def solve(s):
    Majiscule = miniscule = chiffre = 0
    for i in s:
        if (i.isdigit()):
            chiffre+=1
        elif (i.isupper()):
            Majiscule+=1
        else:
            miniscule+=1
            
    if(Majiscule >= 1 and miniscule >= 1 and chiffre>= 1):
        return s
    
    else:
        for i in range(len(s)):
            if (s[i].isdigit()):
                if (chiffre>= 2):
                    if (Majiscule == 0):
                        s[i] = 'S'
                        Majiscule+=1
                        chiffre-=1
                    elif (miniscule == 0):
                        s[i] = 's'
                        miniscule+=1
                        chiffre-=1
            elif (s[i].isupper()):
                if (Majiscule >= 2):
                    if (chiffre== 0):
                        s[i] = "5"
                        chiffre+=1
                        Majiscule-=1
                    elif (miniscule == 0):
                        s[i] = 's'
                        miniscule+=1
                        Majiscule-=1
            elif (s[i].islower()):
                if (miniscule >= 2):
                    if (chiffre== 0):
                        s[i] = "5"
                        chiffre+=1
                        miniscule-=1
                    elif (Majiscule == 0):
        
                        s[i] = 'S'
                        Majiscule+=1
                        miniscule-=1    
    return s


n=int(input())
for i in range(n):
    s=input()
    print(''.join(solve(list(s))))
    