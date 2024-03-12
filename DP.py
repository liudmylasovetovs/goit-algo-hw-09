def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    # Створення списку для збереження мінімальної кількості монет для кожної суми
    min_coins = [float('inf')] * (amount + 1)

    # Створення списку для збереження номіналів монет для кожної суми
    coin_combinations = [{} for _ in range(amount + 1)]

    # Нульова кількість монет для суми 0
    min_coins[0] = 0

    # Ітерація по всіх сумах від 1 до заданої суми
    for i in range(1, amount + 1):
        # Ітерація по всіх доступних номіналах монет
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                # Оновлення мінімальної кількості монет та номіналів
                min_coins[i] = min_coins[i - coin] + 1
                coin_combinations[i] = dict(coin_combinations[i - coin])
                coin_combinations[i][coin] = coin_combinations[i].get(coin, 0) + 1

    return coin_combinations[amount]



amount = 113

result = find_min_coins(amount)
print("Сума:", amount)
print("Оптимальний спосіб видачі решти:", result)



