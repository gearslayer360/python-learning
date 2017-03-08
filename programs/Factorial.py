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
    print(str(num) + "!")
    for i in range(num, 1, -1):
        print(str(i) + "*", end="")
        if i == 2:
            print("1")
        factorial *= i
    print("The factorial of " + str(num) + " is " + str(factorial))
