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


ls = [6, 7, 4, 4, 12, 91, 51, 23, 21]
merge_sort(ls)
print(ls)
