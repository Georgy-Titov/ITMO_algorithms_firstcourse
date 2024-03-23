#сортировка пузырьком
def bubble_sort(ls):
    for step in range(len(ls) - 1):
        for i in range(len(ls) - 1 - step):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]

    return ls


a = [13, 4, 5, 7, 1, 35, 9]
bubble_sort(a)
print(a)

#сортировка при помощи метода .sort()
a.sort()
