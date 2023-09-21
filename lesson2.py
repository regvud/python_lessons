# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
#                                - другий повертає всі записи


def notebook():
    todos_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todos_list
        todos_list.append(todo)

    def get_all() -> list[str]:
        nonlocal todos_list
        return todos_list

    return add_todo, get_all


add1, all1 = notebook()
add2, all2 = notebook()

add1('awake')
add1('awake')

add2('luck')
add2('hug')

print(all1())
print(all2())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)

# Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(number: int) -> str:
    st = str(number)
    length = len(st) - 1
    res: list[str] = []

    for i, v in enumerate(st):
        if v != '0':
            res.append(v + '0' * (length - i))

    return ' + '.join(res) + f' = {st}'


print(expanded_form(500143))


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

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
