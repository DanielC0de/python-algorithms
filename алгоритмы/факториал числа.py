# Легкий метод, которые не работает после 1000
from math import factorial


number = 10


def ez_factorial(n):
    if n == 0:
        return 1

    return ez_factorial(n-1)*n


print(f"факториал числа {number} = {ez_factorial(number)}")

# более хороший метод вычисления факториала
number = 10


def factorial(n):
    if n == 0:
        return 1
    f = 1
    i = 0
    while i < n:
        i += 1
        f *= i
    return f


print(
    f"факториал числа {number} = {factorial(number)}, это крутая функция по вычислению факториала!")
