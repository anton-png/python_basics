"""
Задание 3.

Узнайте у пользователя целое положительное число n.
Найдите сумму чисел n + nn + nnn.

Пример:
Введите число n: 3
n + nn + nnn = 369
"""

n = input('Enter number:')
if n.isdigit():
    n = int(n)
    nn = int('{0}{0}'.format(n))
    nnn = int('{0}{0}{0}'.format(n))
    p_sum = n + nn + nnn
    print("progress sum: %d" % p_sum)