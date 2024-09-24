def Countig(n):
    count=0
    while n>0:
        n=n//10
        count+=1
    return count
sr=int(input('enter a num'))    
er=int(input('enter a num'))    
if sr>er:
    print("incalid")
else:
    for i in range(sr,er+1):
        res=Countig(i)
        print(i,res)    
