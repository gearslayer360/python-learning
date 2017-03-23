"""This program will return all possible combinations of differently priced fruit
 that equals exactly 5 dollars, or 500 cents

 Brian Matthys
 3/20/17
"""

from math import floor

fruits = {}  # Dict of fruits and prices
max_price = 500  # total money we have to spend
max_fruit = []  # maximum number of fruits we can afford for each fruit
answers = []  # solution
fruit_names = []  # list of only names of fruit to reference as a dict key


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

    print("current price " + str(curr_price))  # test string remove later

    if curr_price == max_price:  # If the price is a perfect match, add the answer combo to list of answers and delete current fruit
        return answers.append(answer)
        del max_fruit[0]
    elif curr_price < max_price:  # If the prices don't match, keep adding fruits to the combo and incrementing the price
        for i in range(0, max_fruit[0] - 1):
            print(i)
            if num + 1 < len(fruit_names):  # While there are still fruits to go through in the list
                if i == 0:  # Don't take one of the fruits
                    print("I'm the first")  # test string remove later
                    return calculate((curr_price + i * int(fruits[fruit_names[0]])), answer, num + 1)
                elif i == 1:  # Take only one of the fruits
                    print("I'm the second")  # test string remove later
                    return calculate((curr_price + i * int(fruits[fruit_names[0]])), answer + fruit_names[0] + " " + str(i) + ",", num + 1)
                else:  # Taking more than one of the fruits
                    print("I'm the third")  # test string remove later
                    return calculate((curr_price + i * int(fruits[fruit_names[0]])), answer + fruit_names[0] + "s" + str(i) + ",", num + 1)
    else:
        pass
    return print(answers)

prompt()
calculate(0, " ", 0)
