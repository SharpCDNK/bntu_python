import math

arr = list(map(float, input("Enter arr: ").split()))

def mean(x):
    mn = 0

    for i in x:
        mn += i

    return mn / len(x)


def deviation(x):
    mn = 0
    cur_mean = mean(arr)
    for i in x:
        mn += (i - cur_mean) ** 2

    return math.sqrt(mn / (len(arr) - 1))

print(f"The mean is {mean(arr):.2f}")

print(f"The standart deviation is {deviation(arr):.5f}")
