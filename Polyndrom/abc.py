#--------------polyndrome---------------

n=int(input('enter a num '))
tem=n
rev=0
while n!=0:
    reme=n%10
    rev=(rev*10)+reme
    n=n//10
if tem==rev:
    print('poly')
else:
    print('not')    
        
#--------------polyndrome using Functions---------------


def polyn(n):
    reve=0
    while n!=0:
        remai=n%10
        reve=(reve*10)+remai
        n=n//10
    return reve
n=int(input('enter'))
res=polyn(n)
if n==res:
    print('polyn')
else:
    print('not ploy')    