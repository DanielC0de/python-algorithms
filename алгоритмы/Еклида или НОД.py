def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


print("Нод чисел 30, 18 = ", gcd(30, 18))
