# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
#                                - другий повертає всі записи

def notebook(todos: list) -> ():
    todos_list = []

    def add_todo(todo: list):
        todos_list.append([i for i in enumerate(todo, start=1)])

    add_todo(todos)

    def get_all():
        return todos_list[0]

    return get_all()


print(notebook(['car wash', 'school', 'english']))


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

# Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(number: int) -> str:
    pass


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором, та буде виводити це значення після виконання функцій

def counter(func):
    count = 0

    def inner():
        nonlocal count

        func()
        count += 1
        print(f'counter is {count}')

        print('*' * 20)
        print('\n')

    return inner


@counter
def adder1():
    print("ADDER 1 ")


@counter
def adder2():
    print("ADDER 2")

adder1()
adder2()
adder1()
