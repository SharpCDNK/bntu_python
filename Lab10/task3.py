arr = list(map(int, input("Input arr: ").split()))

counts = [0] * 100

for i in arr:
    counts[i] += 1


for i in range(len(counts)):
    if counts[i] > 0:
        print(f"{i} occurs {counts[i]} time{'s' if counts[i] > 1 else '' }")
