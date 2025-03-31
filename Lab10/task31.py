arr = list(input("Enter str: "))

counts = [0] * 10

for i in arr:
    if i.isdigit():
        counts[int(i)] += 1

for i in range (len(counts)):
    print(f"{i} occurs {counts[i]} time{'s' if counts[i] > 1 else '' }")



