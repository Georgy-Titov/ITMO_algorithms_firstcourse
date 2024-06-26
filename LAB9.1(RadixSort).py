# поразрядная сортировка
def radix_sort(arr):
    if len(arr) == 0:
        return arr
    else:
        # находим размер самого длинного числа
        max_digits = max([len(str(x)) for x in arr])
        # основание системы счисления
        base = 10
        # создаём промежуточный пустой массив из 10 элементов
        bins = [[] for _ in range(base)]
        # перебираем все разряды, начиная с нулевого
        for i in range(0, max_digits):
            # перебираем все элементы в массиве
            for x in arr:
                # получаем цифру, стоящую на текущем разряде в каждом числе массива
                digit = (x // base ** i) % base
                # отправляем число в промежуточный массив в ячейку, которая совпадает со значением этой цифры
                bins[digit].append(x)
            # собираем в исходный массив все ненулевые значения из промежуточного массива
            arr = [x for queue in bins for x in queue]
            # очищаем промежуточный массив
            bins = [[] for _ in range(base)]
        # На тот случай если будут отрицательные числа
        while arr[-1] < 0:
            arr.insert(0, arr.pop())
        # возвращаем отсортированный массив
        return arr


# запускаем сортировку
print([137137105157, 24395739293, 474290561035, 5, 276, 42], "->", radix_sort([137137105157, 24395739293, 474290561035, 5, 276, 42]))
print([], "->", radix_sort([]))
print([1, 2, 3, 12, 13, 14, 25, 23, 21, 123, 321, 320], "->", radix_sort([1, 2, 3, 4, 5]))
print([-12, 131, 0, -12312, -1, 1, 2, 3, 41], "->",radix_sort([-12, 131, 0, -12312, -1, 1, 2, 3, 41]))
