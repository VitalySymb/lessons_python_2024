from datetime import datetime, timezone
from os import path
import exceptions


class Authenticator:
    def __init__(self):
        self.login: str | None = None
        self.password: str | None = None
        self.last_success_login_at: datetime | None = None
        self.errors_count: int = 0

        if self._is_auth_file_exist():
            self._read_auth_file()

    def registrate(self, login: str, password: str):
        """ Registration. Checking a file for absence """
        if self._is_auth_file_exist() or self.login is not None:
            self.errors_count += 1
            raise exceptions.RegistrationError('Такое имя уже есть')

        self.login = login
        self.password = password
        self.last_success_login_at = datetime.now(timezone.utc)
        self._update_auth_file()

    def authorize(self, login: str, password: str):
        """ File verification
            Checking the correspondence of login and password"""
        if self.login is None:
            raise exceptions.AuthorizationError('Такого пользователя нет, нужно зарегистрироваться')

        if not (self.login == login.strip() and self.password == password.strip()):
            self.errors_count += 1
            raise exceptions.AuthorizationError('Не верный логин или пароль, попробуйте еще раз')

        self._update_auth_file()
        print(
            f'Поздравляю {self.login} вы авторизовались!\nВам понадобилась {self.errors_count + 1} попытки\n{self.last_success_login_at.strftime("%d-%m-%y %H:%M:%S")}')

    def _update_auth_file(self):
        """ updating data in a file  """

        with open('auth.txt', 'w') as f:
            f.write(f'{self.login}\n')
            f.write(f'{self.password}\n')
            f.write(f'{self.last_success_login_at.isoformat()}\n')
            f.write(f'{self.errors_count}\n')

    def _read_auth_file(self):
        """ reading from file and defining into variables """

        with open('auth.txt', 'r') as f:
            self.login = f.readline().strip()
            self.password = f.readline().strip()
        self.last_success_login_at = datetime.now(timezone.utc)

    @staticmethod
    def _is_auth_file_exist() -> bool:
        """ checking for file availability """
        return path.exists('auth.txt')
