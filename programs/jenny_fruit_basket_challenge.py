"""This program will return all possible combinations of differently priced fruit
 that equals exactly 5 dollars, or 500 cents

 Brian Matthys
 3/20/17
"""

from math import floor

fruits = {}  # Dict of fruits and prices
max_price = 500  # total money we have to spend
current_price = 0  # current price of all objects being totaled
max_fruit = []  # maximum number of fruits we can afford for each fruit
answers = []  # solution
fruit_names = []


def prompt():
    """Ask the user for the fruits and their prices"""
    while True:
        answer = input(print("Enter a fruit name and price, or enter q to quit:"))

        if answer == "q":
            break
        else:
            parts = answer.split()
            fruits[parts[0]] = parts[1]


def calculate(curr_price, answer, num):
    """Defining a function to solve for the combinations of fruits possible
    using a recursive solution"""
    if num == 0:
        for k, v in fruits.items():
            max_fruit.insert(0, floor(500 / int(fruits[k])))
            fruit_names.append(k)
        max_fruit.sort()
        max_fruit.reverse()
        fruit_names.sort()

    if curr_price == max_price:
        answer = "got one"
        answers.append(answer)
        del max_fruit[0]
    elif curr_price < max_price:
        for i in range(1, max_fruit[0]):
            print(i)
            if num + 1 < len(max_fruit):
                return calculate((curr_price + i * int(fruits[fruit_names[0]])), answer, num+1)  # max_fruit[i]
    else:
        pass


prompt()
calculate(0, " ", 0)

print(answers)
print("answers above")

# Print the formatted result
for key, value in fruits.items():
    if int(value) > 1:
        print(value + " " + key + "s")
    else:
        print("1 " + key)
