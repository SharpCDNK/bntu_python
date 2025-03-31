def custom_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

arr = list(map(int, input("Input arr: ").split()))

ans = arr[0]

for i in arr[1:]:
    ans = custom_gcd(ans,i)

print("GCD of arr: ", ans)
