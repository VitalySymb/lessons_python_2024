# Берём уже то, что вы сделали к последнему уроку.
#
# 0. Обязательно к прочтению Дзен python.
#
# 1. Создать несколько функций на проверку введённых данных:
#
# - Проверка имени
#
# - Проверка возраста Функции должны возвращать строку с ошибкой. Если функции вернули ошибки, нужно вывести
#
# пользователю ошибки.
#
# 2. Улучшить проверку имени: в имени между буквами допускается только 1 пробел.
#
# 3. Сделать совет по получению или замене паспорта (эта задача больше не является со звездочкой) в отдельной функции,
#
# которая возвращает строку.
#
# 4. Создать функцию main, в которой будут вызовы всех остальных функций, ввод данных и прочее.
#
# 5. Создать цикл до тех пор, пока пользователь не введёт верные данные без ошибок.
#
# 6. Создать функцию, которая очищает введённые данные от лишних пробелов в начале и в конце строки.
#
# ### Ограничения:
#
# - Разрешается использовать только два раза print.
#
# - Нельзя использовать глобальные переменные
def del_space(name: str) -> str:
    return name.strip()

def check_name(name: str) -> str:
    text = ''

    if not name:
        text = 'error: Пустая строка'
    elif len(name) < 3:
        text = 'error: Минимальное кол-во символом 3'
    elif name.strip().count(' ') > 1:
        text = 'error: Разрешен один пробел'


    return text


def check_age(age: int) -> int:
    text = ''

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


def main():
    text = ''
    while True:
        if not text:
            name = input('Введите имя: ')
            text = check_name(name)

        if not text:
            age = int(input('Введите возраст: '))
            text = check_age(age)

        if not text:
            print_hello(name, age)
            break

        print(text)
        text = ''

main()