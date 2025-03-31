arr = list(map(int,input("Enter arr: ").split()))

def eliminateDuplicates(lst):
    new_ans = []
    for i in lst:
        if i not in new_ans:
            new_ans.append(i)

    return new_ans


print("New arr: ", eliminateDuplicates(arr))

