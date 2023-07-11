coins = [int(i) for i in input('Введите состояние монет: ').split()]     # Задача 10
count = 0
for i in range(1, len(coins)):
    if coins[i] != coins[i-1]:
        count += 1
print(count)


s = int(input("Введите сумму чисел: "))                   #Задача 12
p = int(input("Введите произведение чисел: "))
found_solution = False

for x in range(1, 1001):
    if found_solution:
        break
    for y in range(1, 1001):
        if x + y == s and x * y == p:
            print("Задуманные числа:", x, y)
            found_solution = True
            break
if not found_solution:
    print("Нет таких чисел х и y")


n = int(input("Введите число: "))                #Задача 14
count = 1
while count <= n:
    count *= 2
    print(count)