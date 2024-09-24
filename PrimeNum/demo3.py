# def Find(n):
#     er=n//2
#     for i in range(2,er+1):
#         if n%i==0:
#             return False
#     return True
# sr=int(input('entr a num'))
# er=int(input('entr a num'))

# for i in range(sr,er+1):
#     if i>1:
#         tem=Find(i)
#         if tem==True:
#             print(i)


# --------------- desending order for prime numbers In functions----------


def another(n):
    er = n // 2
    for i in range(er, 1, -1):
        if n % i == 0:
            return False
    return True


sr = int(input("entr a num"))
er = int(input("entr a num"))
if sr > er:
    print("invalid")
else:
    for i in range(er, sr + 1, -1):
        if i > 1:
            tem = another(i)
            if tem == True:
                print(i)
