string = "Hello world!"


def reverse_string(s):
    chars = list(s)
    for i in range(len(s)//2):
        temp = chars[i]
        chars[i] = chars[len(s)-i-1]
        chars[len(s)-i-1] = temp
    return "".join(chars)


print(string)
print(reverse_string(string))
print("Можно легче и быстрее:", string[::-1])
print("Лучше делай 2-ым вариантом")
