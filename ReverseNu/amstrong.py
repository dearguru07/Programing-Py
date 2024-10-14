
# num = int(input("Enter a number: "))
# order = len(str(num))
# sum = 0

# temp = num
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** order
#     temp //= 10

# if num == sum:
#     print(num, "is an Armstrong number")
# else:
#     print(num, "is not an Armstrong number")



import math

# Function to check if a number is a Strong number
def is_strong_number(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += math.factorial(digit)
        temp //= 10
    return sum == num

# Input from the user
num = int(input("Enter a number: "))

# Check and display the result
if is_strong_number(num):
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")
