n1 = n2 = 1

n = 10

print(n1, end=" ")
print(n2, end=" ")

for i in range(2, n):
    n1, n2 = n2, n1 + n2

    print(n2, end=" ")
