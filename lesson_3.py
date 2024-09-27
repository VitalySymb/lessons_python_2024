
def check_name(name: str) -> tuple:
    text = ''
    if not name.isalpha():
        text = 'the name must consist of letters'

    elif len(name) <= 3:
        text = 'longer than 3 characters'

    return (text, name)

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
    list_func = (check_name, check_age)
    name_age = []
    count = 0
    input_name = ('name', 'age')

    while count < 3:

        if count < 2:
            user_input = input(f'Input {input_name[count]}: ')
            text, parameter = list_func[count](user_input)

            if not text:
                name_age.append(parameter)
                count += 1

        else:
            name = name_age[0].capitalize()
            age = name_age[1]
            text = f'Hello {name}. You are {age} years old.'
            if 16 <= int(age) <= 17:
                text = f"{text} Don't forget to get your first passport."
            elif 25 <= int(age) <= 26 or 45 <= int(age) <= 46:
                text = f"{text} don't forget to replace your passport."
            count += 1

        print(text)


print_name_age()
