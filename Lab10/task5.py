ans = []

arr = list(map(int, input("Enter ten numbers:").split()))

for i in arr:
    if i not in ans:
        ans.append(i)

print("The distinct numbers are: ", end= "")
for i in ans:
    print(i, end=" ")

print()
