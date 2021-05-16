"""
this program generates the probabilities of the sums gotten from rolling two dice
"""

import random


class Dice:
    def roll(self):
        __first = random.randint(1, 6)
        __second = random.randint(1, 6)
        return __first, __second


die1 = Dice()
numerator = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

rolls = 10
for i in range(rolls):
    first, second = die1.roll()
    for j in range(1,13):
        if first + second == j:
            numerator[j-2] += 1

print(f"Rolls: {rolls}")
for i in range(0, 11):
    currentSum = i + 2
    probability = numerator[i]*100/rolls
    print(f"{currentSum}'s: {numerator[i]}")
    print(f"Probability: {probability}%")
print(f"Total: {sum(numerator)}")


