"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_info(**kvargs):
    """
    Displaying user data in one line
    :param str name: Username
    :param str surname: Surname
    :param int year: Year of birth
    :param str city: City of residence
    :param str email: Email
    :param str phone: Phone
    :return: user data string
    """
    name = kvargs.get("name")
    surname = kvargs.get("surname")
    year = kvargs.get("year")
    city = kvargs.get("city")
    email = kvargs.get("email")
    phone = kvargs.get("phone")
    return f"{name} {surname} {year} года рождения, проживает в городе {city}, email: {email}, телефон: {phone}"


print(user_info(name='Paul', surname='Everitt', year=2000, city='Moscow', email='a@b.c', phone='1-46-3'))
