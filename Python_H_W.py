coins = [int(i) for i in input('Введите состояние монет: ').split()]
count = 0
for i in range(1, len(coins)):
    if coins[i] != coins[i-1]:
        count += 1
print(count)   