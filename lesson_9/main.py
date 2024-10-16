from random import randint
import exceptions
import authenticator


def guess_number_game(name: str):
    """Игра "угадай число". Генерирует случайное число,
     которое пользователь должен угадать."""
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
    authentication = authenticator.Authenticator()
    while True:
        if authentication.login is None:
            text = 'Регистрация'
            entrance = authentication.registrate
        else:
            text = 'Авторизация'
            entrance = authentication.authorize

        print(text)
        login = input('Введите логин: ')
        password = input('Введите: ')
        try:
            entrance(login, password)

        except (exceptions.RegistrationError, exceptions.AuthorizationError) as e:
            print(f'Я поймал ошибку: {e}')
            continue

        # guess_number_game(authentication.login)
        break


if __name__ == '__main__':
    main()
