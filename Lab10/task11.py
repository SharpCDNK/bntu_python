import random

arr = list(map(int,input("Enter arr: ").split()))

def shufle(arr):
    for i in range(len(arr)):
        ridx = random.randint(0,len(arr) - 1)

        arr[i],arr[ridx] = arr[ridx], arr[i]

    return arr


print(f"Shuffle of arr: {shufle(arr)}")
