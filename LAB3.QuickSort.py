import random
from timeit import timeit


def quick_sort(s):
    if len(s) <= 1:
        return s

    elem = s[0]
    left = list(filter(lambda x: x < elem, s))
    center = [x for x in s if x == elem]
    right = list(filter(lambda x: x > elem, s))

    return quick_sort(left) + center + quick_sort(right)


a = [random.randint(1, 100) for x in range(1000)]
time = timeit("quick_sort(a)", globals=globals(), number=1000)
print(quick_sort(a))
print(f"Среднее время выполнения алгоритма: {time} сек.")
