from datetime import datetime, timezone
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
        self.data_now = datetime.now(timezone.utc)


class Validator:
    def __init__(self):
        self.data_history: list[Data] = []

    def _validate_name(self):
        """Проверка имени на определенные условия. При нарушении условий
        вызывается ошибка, которая отлавливаешься в main """

        name = self.data_history[-1].name

        if not name:
            raise ValidationError('name error: Пустая строка')
        elif len(name) < 3:
            raise ValidationError('name error: Минимальное кол-во символом 3')
        elif name.strip().count(' ') > 1:
            raise ValidationError('name error: Разрешен один пробел')

    def _validate_age(self):
        """Проверка возраста на определенные условия. При нарушении условий
        вызывается ошибка, которая отлавливаешься в main """

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
        """Получение экземляра класса Data и сохранение в list.
        Вызов метода проверки на условие верных данных пользователя.
        Вызов метода получения и печати времени ввода данных пользователя"""

        self.data_history.append(data)

        self._validate_name()
        self._validate_age()

        self._input_time()

    def _input_time(self):
        """Получаем дату начала/конец ввода данных и сохранения их в формате H:M:S.
        Получаем общее время пользователя, конвертируем их в нужный формат и отображаем."""

        first_time = self.data_history[0].data_now.strftime("%H:%M:%S")
        last_time = self.data_history[-1].data_now.strftime("%H:%M:%S")

        total_time = self.data_history[-1].data_now - self.data_history[0].data_now

        seconds = int(total_time.total_seconds())
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)

        # hours = total_time.seconds // 3600
        # minutes = total_time.seconds % 3600 // 60
        # seconds = total_time.seconds % 3600 % 60

        print(
             f'\nВы сделали {len(self.data_history)} попыток\n'
             f'первая попытка: {first_time}\n'
             f'последняя попытка: {last_time}\n'
             f'общее время: {hours}:{minutes}:{seconds}')
