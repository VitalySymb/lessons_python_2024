# - guess_number_game - игра "угадай число",
# где пользователь вводит число и пытается отгадать
# случайно сгенерированное число от 1 до 5
#
# - Все функций валидации должны всегда возвращать 'None',
# а в случае ошибки - делать raise Exception (текст ошибки).
#
# - В функции 'main' необходимо отловить ошибки из функции validate.
# Вывести пользователю: "Я поймал ошибку: {текст ошибки}.
# И если были ошибки, тогда вам необходимо заново запросить у пользователя ввод данных.

# В функции main обрабатывать ошибку ValueError
#
# - Перед запросом данных в функции "main" пользователю должно печататься
# номер текущей попытки ввода данных.
#
# - Во время игры "угадай число" тоже должен быть счетчик попыток.

# - Пользователю отображать попытки начинаю с 1Б в коде попытки должны быть с 0

from random import randint
def clear_whitespaces(name: str) -> str:
    return name.strip()

def validate_name(name: str) -> None:

    if not name:
        raise Exception('name error: Пустая строка')
    elif len(name) < 3:
        raise Exception('name error: Минимальное кол-во символом 3')
    elif name.strip().count(' ') > 1:
        raise Exception('name error: Разрешен один пробел')



def validate_age(age: int) -> None:

    if age == 0:
        raise Exception('age error: Возраст не может быть 0')
    elif age < 0:
        raise Exception('age error: Возраст не может иметь отрицательное значение')
    elif age < 14:
        raise Exception('age error: Минимальный возраст 14 лет')



def print_hello(name: str, age: int):

    text = f'Привет {name.capitalize()}, тебе {age} лет.'
    if 16 <= age <= 17:
        text = f'{text} Не забудь получить первый паспорт!'
    elif 25 <= age <= 26:
        text = f'{text} Нужно заменить паспорт!'
    elif 45 <= age <= 46:
        text = f'{text} Нужно второй раз заменить паспорт!'

    print(text)

def guess_number_game(name: str):
    game_count = 0
    random_number = randint(1, 5)
    text = f"{name.capitalize()}, угадайте число от 1 до 5:  "
    while True:

        number_user = int(input(text))

        if random_number == number_user:
            text = f'{name.capitalize()}, число {number_user} является верным.'
            print(text)
            break
        else:
            game_count += 1
            text = f'число {number_user+1} не подходит. Твоя {game_count} попытка: '


def main():
    error_counts = 0
    text = f'Введите имя: '
    while True:
        name = input(text)
        text = f'Ваша {error_counts+2} попытка,\nвведите имя: '
        age = input('введите возраст: ')

        try:
            age = int(clear_whitespaces(age))
            validate_name(clear_whitespaces(name))
            validate_age(age)

        except (ValueError, Exception) as e:
            print(f'Я поймал ошибку: {e}')
            error_counts += 1
            continue

        print_hello(name, age)
        guess_number_game(name)
        break


main()