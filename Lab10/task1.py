arr = list(map(int,input("Enter arr: ").split()))

best_mark = max(arr)

for i in range(len(arr)):
    print("Student ", i, " score is ", arr[i], " and grade is ", end = "")

    if arr[i] >= best_mark - 10:
        print("A")
    elif arr[i] >= best_mark - 20:
        print("B")
    elif arr[i] >= best_mark - 30:
        print("C")
    elif arr[i] >= best_mark - 40:
        print("D")
