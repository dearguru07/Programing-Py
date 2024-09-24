# def Prime(n):
#     tem=True
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             tem=False
#             break
#     if tem==True and n>1:
#         print("prime")
#     else:
#         print('not prime')        
# n=int(input('entr a nuumber'))      
# Prime(n)  


def Prime(n):
    er=n//2
    for i in range(2,er+1):
        if n%i==0:
            return False
    return True
sr=int(input('er'))        
er=int(input('er'))      
if sr>er:
    print('invalid range')
else:
    for i in range(sr,er+1):
        if i>1: 
            flag=Prime(i)
            if flag==True:
                print(i)


