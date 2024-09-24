# Polyndrome in given range---------------

def Polyn(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
sr=int(input('entr a num'))    
er=int(input('entr a num'))    
if sr>er:
    print('inalid range')
else:
    for i in range(sr,er+1):    
        res=Polyn(i)
        if i==res:
            print(i)