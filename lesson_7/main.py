# Создать модуль exceptions, в нем класс ValidationError, который наследуется от Exception.
# Никакие методы, свойства переопределять не нужно, необходимо только описать в docstring,
# что это класс ошибки валидации данных.
#
# Создать модуль validator, в котором:
#
# Реализовать класс Data, конструктор которого принимает name и age аргументы,
# сохраняет их в одноименные переменные экземпляра класса. Так же у этого класса должен быть метод _clear_whitespaces,
# который очищает от пробелов в начале и в конце переменные name и age у экземпляра класса. Вызывать метод _clear_whitespaces необходимо из конструктора класса.
#
# Реализовать класс DataWithDate, наследовавшись от класса Data. Конструктор
# должен делать то же самое, что и родительский класс, но дополнительно сохраняет текущее время, когда был создан этот экземпляр класса ( см. datetime.utcnow).
#
# Реализовать класс Validator. У класса Validator должны быть следующие методы:
#
# конструктор класса — в экземпляре класса создает переменную data_history, которая является пустым списком, но будет хранить объекты класса Data.
# _validate_name — валидация имени (скопировать код из функции validate_name).
# _validate_age — валидация возраста (скопировать код из функции validate_age).
# validate — принимает аргумент data (объект класса Data) и сохраняет в список data_history.
# Далее запускает методы валидации, описанные выше.
# При этом методы _validate_name и _validate_age должны брать имя и возраст из переменной Validator.data_history (самое последнее значение).
# А также выбрасывать исключения ValidationError вместо Exception. Если переменная data_history пуста, тогда выбрасывать исключение ValueError.
#
# В вашем основном файле, где вся текущая домашка:
#
# В самом верху необходимо импортировать класс Validator из модуля validator.
# В самом верху необходимо импортировать класс ValidationError из модуля exceptions.
# В функции main до цикла создать объект класса. Вызвать метод validate вместо тех функций валидаций,
# которые были написаны в домашках ранее - эти функции необходимо удалить из этого файла. Обрабатывать ошибку ValidationError вместо Exception.
# После того как пользователь ввел данные, необходимо создать объект класса DataWithDate и далее работать только с ним.
# Теперь количество попыток ввода данных должно выводиться только в том случае, если пользователь не смог с первого раза ввести верные данные.
# После ввода верных данных и до запуска игры необходимо показать пользователю:
# Общее количество попыток
# Время первой попытки, время последней попытки
# Сколько времени понадобилось пользователю, чтобы от первой попытки дойти к последней (формат HH:MM:SS, где HH - часы, MM - минуты, SS - секунды)

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
