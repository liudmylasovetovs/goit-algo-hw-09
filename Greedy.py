def find_coins_greedy(amount):
    """
    Жадібний алгоритм для знаходження оптимального способу видачі решти.

    :param amount: Сума, яку потрібно видати.
    :param coins: Набір монет для видачі.
    :return: Словник із кількістю монет кожного номіналу.
    """
    coins = [50, 25, 10, 5, 2, 1]
    coin_counts = {}

    # Сортуємо монети у спадаючому порядку
    coins.sort(reverse=True)

    for coin in coins:
        # Визначаємо кількість монет даного номіналу, яку можна використовувати
        count = amount // coin
        # Оновлюємо залишок суми
        amount %= coin

        # Додаємо кількість монет даного номіналу до результату, якщо вона не дорівнює нулю
        if count > 0:
            coin_counts[coin] = count

    return coin_counts


amount = 113

result = find_coins_greedy(amount)

print("Сума:", amount)
print("Оптимальний спосіб видачі решти:", result)
