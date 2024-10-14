from datetime import datetime, timezone
from os import path
import exceptions


class Authenticator:
    def __init__(self, login: str = None, password: str = None,
                 last_success_login_at: datetime = None, errors_count: int = 0):
        self.login = login
        self.password = password
        self.last_success_login_at = last_success_login_at
        self.errors_count = errors_count

        if self._is_auth_file_exist():
            self._read_auth_file()

    def _read_auth_file(self):
        list_data_auth = []

        with open('auth.txt') as file:
            for f in file:
                list_data_auth.append(f.rstrip())

        self.login = list_data_auth[0]
        self.password = list_data_auth[1]
        self.last_success_login_at = datetime.fromisoformat(list_data_auth[2])  # из str в datetime
        self.errors_count = int(list_data_auth[3])

    def _is_auth_file_exist(self) -> bool:
        if path.exists('auth.txt'):
            return True
        return False

    def registrate(self, login: str, password: str):
        if self._is_auth_file_exist() or self.login is not None:
            raise exceptions.RegistrationError('Пользователь уже существует')

        with open('auth.txt', 'w') as file:
            file.write(f'{login}\n'
                       f'{password}\n'
                       f'{datetime.now(timezone.utc)}\n'
                       f'{self.errors_count}\n')
        self._read_auth_file()

    def authorize(self, login: str, password: str):
        if self.login is None:
            raise exceptions.AuthorizationError('Такого пользователя нет, нужно зарегистрироваться')

        with open('auth.txt') as f:
            data_list = f.readlines()
            login_data = data_list[0].strip()
            password_data = data_list[1].strip()

        if login_data == login.strip() and password_data == password.strip():
            self._update_auth_file()
            print(
                f'Поздравляю {self.login} вы авторизовались!\nВам понадобилась с {self.errors_count + 1} попытки\n{self.last_success_login_at.strftime("%d-%m-%y %H:%M:%S")}')
        else:
            self.errors_count += 1
            raise exceptions.AuthorizationError('Не верный логин или пароль, попробуйте еще раз')

    def _update_auth_file(self):
        self.last_success_login_at = datetime.now(timezone.utc)
        with open('auth.txt', 'r') as f:
            list_data = f.readlines()

        list_data[2] = f'{self.last_success_login_at}\n'
        list_data[3] = f'{self.errors_count}\n'

        with open('auth.txt', 'w') as f:
            f.writelines(list_data)
