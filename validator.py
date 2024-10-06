class Data:
    def __init__(self, name: str, age: str):
        self.name = self._clear_whitespaces(name)
        self.age = self._clear_whitespaces(age)

    def _clear_whitespaces(self, text: str):
        return text.strip()
