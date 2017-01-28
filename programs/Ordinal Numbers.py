# This program will print numbers from 1 to 1000
# and with their correct ending such as "st", "nd", "rd", or "th"

numbers = []

for i in range(1, 1001):
    numbers.append(i)

ending = ""

for number in numbers:
    if number % 10 == 1:
        ending = "st"

    elif number % 10 == 2:
        ending = "nd"

    elif number % 10 == 3:
        ending = "rd"

    else:
        ending = "th"

    print(str(number) + ending)
