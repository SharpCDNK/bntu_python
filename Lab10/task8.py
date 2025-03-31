import sys

arr = list(map(int,input("Tnter arr: ").split()))

def indexOfSmallestElement(lst):
    ans_idx = -1
    ans_el = sys.maxsize

    for i in range(len(lst)):
        if lst[i] < ans_el:
            ans_el = lst[i]
            ans_idx = i

    return ans_el, ans_idx

p_el, p_idx = indexOfSmallestElement(arr)

print(p_el, " ", p_idx)
