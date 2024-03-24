def quick_sort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [x for x in s if x == elem]
    right = list(filter(lambda x: x > elem, s))

    return quick_sort(left) + center + quick_sort(right)



def find_min_max(sequence):
    if len(sequence) == 0:
        return [0, 0]
    min_max = [sequence[0], sequence[0]]
    for element in sequence:
        if element < min_max[0]:
            min_max[0] = element
        if element > min_max[1]:
            min_max[1] = element
    return min_max


def bucket_sort(s, n):
    buckets = []
    for i in range(n):
        buckets.append([])
    min_max = find_min_max(s)
    if min_max[0] == min_max[1]:
        return s
    for element in s:
        buckets[(n * (element - min_max[0])) // (min_max[1] - min_max[0] + 1)].append(element)
    print(buckets)
    for i in range(len(buckets)):
        if len(buckets[i]) <= 32:
            buckets[i] = quick_sort(buckets[i])
        else:
            bucket_sort(buckets[i], n)
    insert_index = 0
    for bucket in buckets:
        for element in bucket:
            s[insert_index] = element
            insert_index += 1


ls = [6, 7, 4, 4, 12, 91, 51, 23, 21]
bucket_sort(ls, 5)
print(ls)
