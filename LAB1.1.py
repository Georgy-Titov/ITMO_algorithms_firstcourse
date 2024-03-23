a = [5, 9, 13, 23, 27, 51, 61, 77, 84, 96]
n = int(input())


def binary_search(ls, search):
    left = 0
    right = len(a) - 1
    mid = (left + right) // 2

    steps = 0

    while search != ls[mid] and left < right:
        steps += 1
        if search > ls[mid]:
            left = mid + 1
        else:
            right = mid - 1

        mid = (left + right) // 2

    if search == ls[mid]:
        print(f"Index: {mid} Search: {search} Steps: {steps}\n")
    else:
        print("Number was not found!\n")


binary_search(sorted(a), n)
