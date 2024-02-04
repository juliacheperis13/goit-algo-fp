import random
from collections import defaultdict

import matplotlib.pyplot as plt

nums = 1_000_000

counts = defaultdict(int)

i = 2
while i < 13:
    counts[i] = 0
    i = i + 1

for _ in range(nums):
    dice = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    counts[dice + dice_two] += 1

probabilities = {key: count / nums for key, count in counts.items()}

title = f"{'Sum':<5} | {'Probability':<5}"

print(" " * len(title))
print(title)
print(" " * len(title))
print("-" * len(title))

for dice, prob in probabilities.items():
    print(f"{dice:<5} | {prob:.2%}{'':<5}")
    print("-" * len(title))


# plt.bar(probabilities.keys(), probabilities.values())
# plt.show()
