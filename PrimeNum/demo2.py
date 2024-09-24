# -----------------Prime Number using Functions (in given Range)-------------------

def CheckPrime(n):
    er = n // 2
    for i in range(2, er + 1):
        if n % i == 0:
            return False
    return True

sr = int(input("enter a sr num"))
er = int(input("enter a er num"))
if sr > er:
    print("invalid range ")
else:
    for i in range(sr, er + 1):
        if i > 1:
            flag = CheckPrime(i)
            if flag == True:
                print(i)
