#This program calculates and prints the factorial of a number
#3/5/2017

num = 0
factorial = 1


def prompt():
    num = input(print("Enter a number:"))
    num = int(num)

    while num < 0:
        print("Factorial doesn't exist for negative numbers, try again")
        num = input(print("Enter a number:"))
        num = int(num)

    return num

num = prompt()

if num == 0:
    print("The factorial of 0 is 1")

else:
    for i in range(1, num+1):
        factorial *= i
    print("The factorial of " + str(num) + " is " + str(factorial))
