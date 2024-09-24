# def Count(n):
#     countD=0
#     while n!=0:
#         n=n//10
#         countD+=1
#     return countD
# n=int(input('entr a number'))    
# res=Count(n)
# print(res)


def countD(n):
    count=0
    while n!=0:
        n=n//10
        count+=1
    return count
sr=int(input('entr a number'))    
er=int(input('entr a number'))  
for i in range(sr,er+1):
    res=countD(i)
    print(i,"digits are",res)  