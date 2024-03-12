
Висновки:

Жадібний алгоритм (find_coins_greedy):
Час виконання: Жадібний алгоритм має простий та швидкий спосіб визначення решти, оскільки обирає найбільший доступний номінал монети. Він часто працює ефективно для невеликих сум грошей.

Алгоритм динамічного програмування (find_min_coins):
Час виконання: Алгоритм динамічного програмування має більший час виконання через використання додаткової таблиці та перебору можливих комбінацій монет. Однак він може бути більш ефективним для великих сум грошей, оскільки шукає оптимальний спосіб формування суми.

Порівняння:

Для невеликих сум (наприклад, 113):
Жадібний алгоритм може працювати досить добре та швидко формувати решту.
Алгоритм динамічного програмування може мати трошки більший час виконання, але це може бути непомітним для менших сум.

Для великих сум (наприклад, 1000):
Жадібний алгоритм може стати менш ефективним, оскільки може вибирати більше монет, що не призводить до мінімальної кількості монет.
Алгоритм динамічного програмування може виявити себе ефективнішим, оскільки знаходить оптимальний шлях для формування суми.

Загальний висновок:
Обидва алгоритми мають свої переваги та недоліки.
Жадібний алгоритм підходить для швидкої видачі решти при невеликих сумах.
Алгоритм динамічного програмування ефективніший для великих сум та гарантує знаходження оптимального варіанту.
