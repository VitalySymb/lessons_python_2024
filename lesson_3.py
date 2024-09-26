# Проверяет правильность ввода имени

def check_name(name: str) -> tuple:
    text = ''
    if not name.isalpha():
        text = 'the name must consist of letters'

    elif len(name) <= 3:
        text = 'longer than 3 characters'

    return (text, name)


# Проверяет правильности ввода возраста
def check_age(age: str) -> tuple:
    text = ''
    if not age.isdigit():
        text = 'You need to enter a number: '

    elif int(age) == 0:
        text = 'age cannot be 0'

    elif int(age) < 14:
        text = 'age cannot be less than 14'

    return (text, age)


def print_name_age():
    list_func = [check_name, check_age]
    name_age = []
    count = 0

    while len(name_age) >= count:
        # условие, при котором запустим все check функций

        if len(name_age) < len(list_func):
            input_name = ('name', 'age')
            text = ''
            func = list_func[count](input(f'Input {input_name[count]}: '))
            if func[0]:
                text = func[0]
            else:
                name_age.append(func[1])
                count += 1
        else:
            count += 1
            name = name_age[0].capitalize()
            age = name_age[1]

            text = f'Hello {name}. You are {age} years old.'

            if 16 <= int(age) <= 17:
                text = f"{text} Don't forget to get your first passport."
            elif 25 <= int(age) <= 26 or 45 <= int(age) <= 46:
                text = f"{text} don't forget to replace your passport."

        print(text)


print_name_age()
