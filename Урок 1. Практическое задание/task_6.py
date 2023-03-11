"""
Задание 6.

Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
Требуется определить номер дня,
на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b
 и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""


# task 6
def one_finance():
    n = input('Net profit:')
    p = input('Proceeds:')
    if n.isdigit() and p.isdigit():
        n = int(n)
        p = int(p)
        x = n / p * 100
        print(f"Profitability: {x}%")
        h = int(input('How many workers:'))
        s = n / h
        print(f"profit per one: {s}")
    else:
        return one_finance()


# task 7
def athlete_result():
    a = input('distance in 1 day (km):')
    b = input('all distance (km):')
    if a.isdigit() and b.isdigit():
        d = 1
        a = int(a)
        b = int(b)
        while a < b:
            a = a / 100 * 10 + a
            d += 1
        return print(d)
    else:
        return athlete_result()


one_finance()
athlete_result()
