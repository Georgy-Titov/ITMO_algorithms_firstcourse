def swap(s, i, j):
    s[i], s[j] = s[j], s[i]


def sift_down(s, i, upper):
    while True:
        l, r = i * 2 + 1, i * 2 + 2
        if max(l, r) < upper:
            if s[i] >= max(s[l], s[r]):
                break
            elif s[l] > s[r]:
                swap(s, i, l)
                i = l
            else:
                swap(s, i, r)
                i = r
        elif l < upper:
            if s[l] > s[i]:
                swap(s, i, l)
                i = l
            else:
                break
        elif r < upper:
            if s[r] > s[i]:
                swap(s, i, r)
                i = r
            else:
                break
        else:
            break


def heap_sort(s):
    for i in range((len(s) - 2) // 2, -1, -1):
        sift_down(s, i, len(s))

    for end in range(len(s) - 1, 0, -1):
        swap(s, 0, end)
        sift_down(s, 0, end)


ls = [5, 0, -2, 7, 3]
heap_sort(ls)
print(ls)
