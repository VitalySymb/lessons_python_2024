from datetime import datetime


class Data:
    def __init__(self, name: str, age: str):
        self.name = self._clear_whitespaces(name)
        self.age = self._clear_whitespaces(age)

    def _clear_whitespaces(self, text: str):
        return text.strip()


class DataWithDate(Data):
    def __init__(self):
        self.current_dateTime = datetime.now()


class Validator:
    def __init__(self):
        self.data_history = []

    def _validate_name(self, name):
        if not name:
            raise ValidationError('name error: Пустая строка')
        elif len(name) < 3:
            raise ValidationError('name error: Минимальное кол-во символом 3')
        elif name.strip().count(' ') > 1:
            raise ValidationError('name error: Разрешен один пробел')

    def _validate_age(self, age):
        if age == 0:
            raise ValidationError('age error: Возраст не может быть 0')
        elif age < 0:
            raise ValidationError('age error: Возраст не может иметь отрицательное значение')
        elif age < 14:
            raise ValidationError('age error: Минимальный возраст 14 лет')


    def validate(self, data):
        pass