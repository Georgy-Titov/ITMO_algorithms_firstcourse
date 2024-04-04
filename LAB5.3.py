def func(sequence):
    n = len(sequence)
    start = 0
    current_length = 1
    max_length = 0
    max_start = 0

    for i in range(1, n):
        if sequence[i] > sequence[i - 1]:
            current_length += 1
        else:
            current_length = 1
            start = i

        if current_length > max_length:
            max_length = current_length
            max_start = start

    return sequence[max_start:max_start + max_length]



print(func([1, 2, 4, 7, -1, 1, 2, 3, 4, 5, 0, 1, 2]))
