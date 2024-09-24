'''
tem=False
n=int(input("enter a number"))
end=n//2
for i in range(2,end+1):
    if n%i==0:
        tem=True
        break
if tem==False and n>2:
    print("prime")
else:
    print("not")    
        
'''  
#---------prime Numbers using Decrememt looop--------
    
# tem=True
# n=int(input("enter"))     
# end=n//2
# for i in range(end,1,-1):
#     if n%i==0:
#         tem=False
#         break
# if tem==True and n>2:
#     print("prime")
# else:
#     print("not")           
    
    
#-------------Prime Number Using Functions-------------
    
def CheckPrime(n):
    tem=True
    er=n//2
    for i in range(2,er+1):
        if n%i==0:
            tem=False
            break
    if tem==True and n>2:
        print("prime")
    else:
        print("not a prime")
n=int(input("enter a number"))
CheckPrime(n)