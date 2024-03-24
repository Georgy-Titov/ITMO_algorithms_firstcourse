import random
from timeit import timeit


def comb_sort(s):
    step = int(len(s) / 1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(s):
            if s[i] > s[i + step]:
                s[i], s[i + step] = s[i + step], s[i]
                swap += 1
            i += 1
        if step > 1:
            step = int(step / 1.247)


a = [random.randint(1, 100) for x in range(1000)]
time = timeit("comb_sort(a)", globals=globals(), number=1000)
comb_sort(a)
print(a)
print(f"Среднее время выполнения алгоритма: {time} сек.")
