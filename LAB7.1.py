def string_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    return "".join(map(str, fibonacci_sequence))


def find_number(string):
    result = {}
    for i in range(len(string) - 1):
        number = int(string[i: i + 2])
        if 10 <= number < 100:
            if number not in result:
                result[number] = 1
            else:
                result[number] += 1

    most_frequent_number_in_string = max(result, key=result.get)
    return most_frequent_number_in_string


s = string_fibonacci_sequence(500)
template = str(find_number(s))


# Наивный алгоритм
def naive_search(text, sub_text):
    c = 0
    sub_text_len = len(sub_text)
    for i in range(len(text) - sub_text_len + 1):
        if text[i:i + sub_text_len] == sub_text:
            c += 1

    return c


# Алгоритм Рабина-Карпа
def Rabin_Carp(text, sub_text):
    c = 0
    sub_text_hash = hash(sub_text)
    sub_text_len = len(sub_text)
    for i in range(len(text) - sub_text_len + 1):
        if hash(text[i: i + sub_text_len]) == sub_text_hash:
            if text[i: i + sub_text_len] == sub_text:
                c += 1

    return c


# Алгоритм Бойера-Мура-Хорспула
def preprocess(substring, start_index, end_index):
    alphabet = [len(substring) for _ in range(end_index - start_index + 1)]
    for i in range(len(substring) - 1):
        alphabet[ord(substring[i]) - start_index] = len(substring) - i - 1
    return alphabet


def bmh(text, substring):
    if len(substring) > len(text):
        return None
    c = 0
    i = len(substring) - 1
    n = i
    start_index = ord(" ")
    end_index = ord("~")
    alphabet = preprocess(substring, start_index, end_index)
    while i < len(text):
        if text[i - n: i + 1] == substring:
            c += 1
        i = i + alphabet[ord(text[i]) - start_index]

    return c


# Алгоритм Кнута-Морриса-Пратаа
def prefix_func(needle):
    m = len(needle)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and needle[k] != needle[q]:
            k = pi[k - 1]
        if needle[k] == needle[q]:
            k += 1
        pi[q] = k
    return pi


def kmp(haystack, needle):
    k = 0
    n = len(haystack)
    m = len(needle)
    prefix = prefix_func(needle)
    q = 0
    for i in range(n):
        while q > 0 and needle[q] != haystack[i]:
            q = prefix[q - 1]
        if needle[q] == haystack[i]:
            q += 1
        if q == m:
            k += 1
            q = prefix[q - 1]
    return k


print(naive_search(s, template))
print(Rabin_Carp(s, template))
print(bmh(s, template))
print(kmp(s, template))
