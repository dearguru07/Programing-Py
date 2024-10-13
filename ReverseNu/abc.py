# n=int(input('enter a num'))
# rev=0
# while n!=0:
#     rem=n%10
#     rev=(rev*10)+rem
#     n=n//10
# print(rev)    


# n=int(input('enter a nub'))
# rev=0
# while n!=0:
#     remainder=n%10
#     rev=remainder+(rev*10)
#     n=n//10
# print(rev) 



def Reverse(n):
    rev=0
    while n!=0:
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return rev
n=int(input('enter a numb'))
res=Reverse(n)
print(res)    

