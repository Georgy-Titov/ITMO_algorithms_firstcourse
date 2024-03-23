# O(3n)
def pas3n(n):
    for i in range(n):
        pass
    for i in range(n):
        pass
    for i in range(n):
        pass


# O(n*log(n))
def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]

    return c


def merge_sort(n):
    if len(n) == 1:
        return n

    middle = len(n) // 2
    left = merge_sort(n[:middle])
    right = merge_sort(n[middle:])
    return merge_two_list(left, right)


# O(n!)
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)


# O(n^3)
def passn3(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass


# O(3*log(n))
def binary_search(ls, search):
    left = 0
    right = len(ls) - 1
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


def binary_search_x3():
    for i in range(3):
        a = [int(x) for x in input().split()]
        a.sort()
        s = int(input())
        binary_search(a, s)


binary_search_x3()
