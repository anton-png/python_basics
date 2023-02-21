"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


def divide(*args):
    """
    divide x by y
    :param int|float x: number
    :param int|float y: number
    :return: x / y
    """
    try:
        return args[0] / args[1]
    except ZeroDivisionError:
        return 'Вы что? Пытаетесь делить на 0!'


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
print(divide(a, b))
