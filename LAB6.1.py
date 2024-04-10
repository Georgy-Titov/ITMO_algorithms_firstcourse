from random import random

string = input("Введите слово: ")
c = random()
m = len(string)

for i in string:
    k = ord(i)
    print(int(m * ((k * c) % 1)), end="")
