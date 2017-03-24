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

weights = {
    'apple': 2,
    'banana': 1,
    'coconut': 5,
    'grapefruit': 3,
    'jackfruit': 8,
    'kiwi': 1,
    'lemon': 1,
    'mango': 2,
    'orange': 2,
    'papaya': 3,
    'pear': 1,
    'pineapple': 8,
    'watermelon': 10
}

budget = 500
payload = 12
solutionCount = 0
iterations = 0


def min(a, b):
    if a > b: return b
    return a


def shop(currentPrice, currentWeight, basket, fruitList):
    global solutionCount, iterations
    iterations = iterations + 1
    if currentPrice == budget:
        print(basket + str(currentWeight) + ", " + str(currentPrice))
        solutionCount = solutionCount + 1
    elif currentPrice < budget and currentWeight < payload:
        while len(fruitList) > 0:
            fruit = fruitList.pop()
            cost = fruits[fruit]
            weight = weights[fruit]
            nfruitByCost = int((budget - currentPrice) / cost)
            nfruitByWeight = int((payload - currentWeight) / weight)
            nfruit = min(nfruitByCost, nfruitByWeight)
            for i in range(1, nfruit + 1):
                newList = list(fruitList)
                newBasket = basket + str(i) + " " + fruit
                if i > 1: newBasket += "s"
                newBasket += ", "
                shop(currentPrice + (i * cost), currentWeight + (i * weight), newBasket, newList)


shop(0, 0, "", list(fruits.keys()))

print("in " + str(iterations) + " iterations, found " + str(solutionCount) + " solutions, for a payload of " + str(payload) + " and a budget of " + str(budget))





