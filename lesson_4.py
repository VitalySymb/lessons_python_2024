# 3. Функции на проверку имени, возраста и совет паспорт должны возвращать None
# (иначе говоря, ничего не должны возвращать), если не было ошибок или нет советов
#
# 4. Сделать функцию, которая генерирует случайное число от 0 до 10,
# и в бесконечном цикле просит пользователя угадать это число,
# если пользователь ввёл имя и возраст корректные
from random import randint
def del_space(name: str) -> str:
    return name.strip()

def check_name(name: str) -> str:
    text = None

    if not name:
        text = 'error: Пустая строка'
    elif len(name) < 3:
        text = 'error: Минимальное кол-во символом 3'
    elif name.strip().count(' ') > 1:
        text = 'error: Разрешен один пробел'


    return text


def check_age(age: int) -> int:
    text = None

    if age == 0:
        text = 'error: Возраст не может быть 0'
    elif age < 0:
        text = 'error: Возраст не может иметь отрицательное значение'
    elif age < 14:
        text = 'error: Минимальный возраст 14 лет'


    return text

def print_hello(name, age):

        text = f'Привет {name.capitalize()}, тебе {age} лет.'
        if 16 <= age <= 17:
            text = f'{text} Не забудь получить первый паспорт!'
        elif 25 <= age <= 26:
            text = f'{text} Нужно заменить паспорт!'
        elif 45 <= age <= 46:
            text = f'{text} Нужно второй раз заменить паспорт!'

        print(text)

def number_generation(name: str):
    random_number = randint(1, 10)
    text = f"{name.capitalize()}, угадайте число от 1 до 10: "
    while True:

        number_user = int(input(text))

        if random_number == number_user:
            text = f'{name.capitalize()}, число {number_user} является верным.'
            print(text)
            break
        else:
            text = f'число {number_user} не подходит. Попробуй еще раз: '


def main():
    text = None
    while True:
        if text is None:
            name = input('Введите имя: ')
            text = check_name(name)

        if text is None:
            age = int(input('Введите возраст: '))
            text = check_age(age)

        if text is None:
            print_hello(name, age)
            number_generation(name)
            break

        print(text)
        text = None

main()