#Проверяет правильность ввода имени
def chech_name() -> str:
    def print_error_name(error_name: str):
        print(error_name)

    while True:
        name_input = input('enter your name: ')
        if not name_input.isalpha():
            print_error_name('the name must consist of letters')

        elif len(name_input) <= 3:
            print_error_name('longer than 3 characters')

        else:
            break

    return name_input

#Проверяет правильности ввода возраста
def check_age() -> int:
    def print_error_age(error_age: str):
        print(error_age)

    while True:
        age_input = input('enter your age: ')

        if not age_input.isdigit():
            print_error_age('You need to enter a number: ')
        elif int(age_input) == 0:
            print_error_age('age cannot be 0')

        elif int(age_input) < 14:
            print_error_age('age cannot be less than 14')

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
print(hello_print)


