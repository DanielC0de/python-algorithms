
def dist(a, b):
    def rec(i, j):
        if i == 0 or j == 0:
            # если первая строка пустая, то растояние равняется ее длине (n вставок)
            return max(i, j)
        elif a[i-1] == b[j-1]:
            # если последние символы одинаковы, то просто съедаем их
            return rec(i-1, j-1)
        else:
            # иначе считаем минимальный вариант
            return 1 + min(
                rec(i, j-1),  # удаление символа
                rec(i-1, j),  # вставка символа
                rec(i-1, j-1),  # замена символа
            )
    return rec(len(a), len(b))


str1 = "Привет"
str2 = "Приветики"

lev = dist(str1, str2)
bigger = max([len(str1), len(str2)])
pct = ((bigger - lev) / bigger) * 100
print(f"Строка 1: {str1}\nСтрока 2: {str2}\n==============\nСхожесть: {pct}%")
