def countD(n):
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count
def Amsrtong(n):
    tem=n
    sum=0
    power=countD(n)
    while n!=0:
        rem=n%10
        sum=(sum+rem**power)
        n//=10
    if tem==sum:
            return True
    else:
            return False
n=int(input('entera number'))          
flag=Amsrtong(n)
if flag==True:
    print('amrg')
else:
    print('not a amstrng')