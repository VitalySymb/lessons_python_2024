def check_name(name: str) -> str:
    text = ''
    if not name.isalpha():
        text = 'the name must consist of letters'

    elif len(name) <= 3:
        text = 'longer than 3 characters'

    return text


def check_age(age: str) -> str:
    text = ''
    if not age.isdigit():
        text = 'You need to enter a number: '

    elif int(age) == 0:
        text = 'age cannot be 0'

    elif int(age) < 14:
        text = 'age cannot be less than 14'

    return text


def print_name_age():
    name = 'name'
    age = 'age'
    count = 0
    flag = True

    while flag:

        if count < 2:
            if count == 0:
                user_input = input(f'Input {name}: ')
                text = check_name(user_input)
            elif count == 1:
                user_input = input(f'Input {age}: ')
                text = check_age(user_input)

            if not text:

                if count == 0:
                    name = user_input
                elif count == 1:
                    age = user_input

                count += 1
                continue

        else:
            text = f'Hello {name.capitalize()}. You are {age} years old.'
            if 16 <= int(age) <= 17:
                text = f"{text} Don't forget to get your first passport."
            elif 25 <= int(age) <= 26 or 45 <= int(age) <= 46:
                text = f"{text} don't forget to replace your passport."
            flag = False

        print(text)


print_name_age()
