"""This program will return all possible combinations of differently priced fruit
 that equals exactly 5 dollars, or 500 cents

 Brian Matthys
 3/20/17
"""

from math import floor

fruits = {
    'apple': 59,
    'banana': 32,
    'coconut': 155,
    'grapefruit': 128,
    'jackfruit': 1100,
    'kiwi': 41,
    'lemon': 70,
    'mango': 97,
    'orange': 73,
    'papaya': 254,
    'pear': 37,
    'pineapple': 399,
    'watermelon': 500
}

max_price = 500  # total money we have to spend
solutions = 0  # total number of solutions


def calculate(curr_price, basket, fruit_list):
    """Defining a function to solve for the combinations of fruits possible
    using a recursive solution"""

    global solutions

    if curr_price == max_price:  # If the price is a perfect match, add the answer combo to list of answers and delete current fruit
        print(basket + str(curr_price))
        solutions += 1
    elif curr_price < max_price:  # If the prices don't match, keep adding fruits to the combo and incrementing the price
        while len(fruit_list) > 0:
            fruit = fruit_list.pop()
            cost = fruits[fruit]
            nfruit = int((max_price - curr_price) / cost)

            for i in range(1, nfruit + 1):
                newList = list(fruit_list)
                newBasket = basket + str(i) + " " + fruit
                if i > 1:
                    newBasket += "s"
                newBasket += ", "
                calculate(curr_price+(i * cost), newBasket, newList)

calculate(0, " ", list(fruits.keys()))
print("found " + str(solutions) + " solutions, for a budget of " + str(max_price))
