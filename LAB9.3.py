def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def subarrays_with_prime_sum(arr):
    subarrays = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarray = arr[i:j + 1]
            if is_prime(sum(subarray)):
                subarrays.append(subarray)
    return subarrays


array = [1, 2, 3, 4, 5]
result = subarrays_with_prime_sum(array)
print("Подмассивы с суммой, являющейся простым числом:", *result)
