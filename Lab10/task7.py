import random

counts = [0] * 10

for j in range(0, 1000):
    i = random.randint(0,9)
    counts[i] += 1

for i in range(len(counts)):
    print(f"{i} occurs {counts[i]} time{'s' if counts[i] > 1 else '' }")

