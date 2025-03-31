arr = list(map(int, input("Input arr: ").split()))

for i in range(len(arr) - 1, -1, -1):
    print(arr[i],end = " ")
