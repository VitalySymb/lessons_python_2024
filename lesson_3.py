#Проверяет правильность ввода имени
def print_text(text: str):
    print(text)

def chech_name() -> str:

    while True:
        name_input = input('enter your name: ')
        if not name_input.isalpha():
            print_text('the name must consist of letters')

        elif len(name_input) <= 3:
            print_text('longer than 3 characters')

        else:
            break

    return name_input

#Проверяет правильности ввода возраста
def check_age() -> int:

    while True:
        age_input = input('enter your age: ')

        if not age_input.isdigit():
            print_text('You need to enter a number: ')
        elif int(age_input) == 0:
            print_text('age cannot be 0')

        elif int(age_input) < 14:
            print_text('age cannot be less than 14')

        else:
            break

    return int(age_input)


name = chech_name().capitalize()
age = check_age()

hello_print = f'Hello {name}. You are {age} years old.'

if 16 <= age <= 17:
    hello_print = f"{hello_print} Don't forget to get your first passport."
elif 25 <= age <= 26 or 45 <= age <= 46:
    hello_print = f"{hello_print} don't forget to replace your passport."
print_text(hello_print)


