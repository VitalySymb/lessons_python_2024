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
import validator
import exceptions


def print_hello(name: str, age: str):
    age = int(age)
    text = f'Привет {name.capitalize()}, тебе {age} лет.'
    if 16 <= age <= 17:
        text = f'{text} Не забудь получить первый паспорт!'
    elif 25 <= age <= 26:
        text = f'{text} Нужно заменить паспорт!'
    elif 45 <= age <= 46:
        text = f'{text} Нужно второй раз заменить паспорт!'

    print(f'\n{text}')


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
            text = f'число {number_user + 1} не подходит. Твоя {game_count} попытка: '


def main():
    validation = validator.Validator()
    error_counts = 0
    text = 'Введите имя: '
    while True:
        name = input(text)
        text = f'Ваша {error_counts + 2} попытка,\nвведите имя: '
        age = input('введите возраст: ')
        name_age_date_time = validator.DataWithDate(name, age)

        try:
            validation.validate(name_age_date_time)

        except exceptions.ValidationError as e:
            print(f'Я поймал ошибку: {e}')
            error_counts += 1
            continue
        text = validation.input_time()
        print(text)

        name = name_age_date_time.name
        age = name_age_date_time.age

        print_hello(name, age)
        guess_number_game(name)
        break


main()
