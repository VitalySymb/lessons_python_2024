from datetime import datetime
from exceptions import ValidationError


class Data:
    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self._clear_whitespaces()

    def _clear_whitespaces(self):
        self.name = self.name.strip()
        self.age = self.age.strip()


class DataWithDate(Data):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.data_now = datetime.now()


class Validator:
    def __init__(self):
        self.data_history = []

    def _validate_name(self):

        name = self.data_history[-1].name

        if not name:
            raise ValidationError('name error: Пустая строка')
        elif len(name) < 3:
            raise ValidationError('name error: Минимальное кол-во символом 3')
        elif name.strip().count(' ') > 1:
            raise ValidationError('name error: Разрешен один пробел')

    def _validate_age(self):

        age = self.data_history[-1].age

        if not age.isdigit():
            raise ValidationError('age error: Нужно ввести число')

        age = int(age)

        if age == 0:
            raise ValidationError('age error: Возраст не может быть 0')
        if age < 0:
            raise ValidationError('age error: Возраст не может иметь отрицательное значение')
        if age < 14:
            raise ValidationError('age error: Минимальный возраст 14 лет')

    def validate(self, data: Data):
        self.data_history.append(data)

        self._validate_name()
        self._validate_age()

        self._input_time()

    def _input_time(self):

        first_time = self.data_history[0].data_now.strftime("%H:%M:%S")
        last_time = self.data_history[-1].data_now.strftime("%H:%M:%S")

        total_time = self.data_history[-1].data_now - self.data_history[0].data_now
        horse = total_time.seconds // 3600
        minutes = total_time.seconds % 3600 // 60
        seconds = total_time.seconds % 3600 % 60
        print(
            f'\nВы сделали {len(self.data_history)} попыток\nпервая попытка: {first_time}\nпоследняя попытка: {last_time}\nобщее время: {horse}:{minutes}:{seconds}')
