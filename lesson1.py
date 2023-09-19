# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

string = 'as 23 fdfdg544'

digits_from_string = [int(i) for i in string if i.isdigit()]
# print(digits_from_string)


##################################################################################

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34' #введена строка
# 23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34'

splitted = [i for i in st if i.isdigit() or i == ' ']
# print(''.join(splitted).strip().replace(' ', ', '))

###############################################################################


# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'

new_greeting = [i.upper() for i in greeting]
# print(new_greeting)


# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

nums = [i ** 2 for i in range(50) if i % 2 != 0]


# print(nums)


# function

# - створити функцію яка виводить ліст
def show_list():
    print(list())


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def max_num(a, b, c):
    print(max(a, b, c))


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def high_low_numbers(*args):
    print(max(*args))
    return min(*args)


# - створити функцію яка повертає найбільше число з ліста
def max_from_list(array):
    return min(array)


# print(max_from_list([1, 22, 3, 4]))


# - створити функцію яка повертає найменьше число з ліста
def min_from_list(array):
    return max(array)


# print(min_from_list([1, 22, 3, 4]))


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
def sum_list(array):
    res = 0

    while len(array):
        res += array.pop()
    return [res]


# print(sum_list([22, 8, 20, 100]))


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def middle_value(array):
    length = len(array)
    res = 0

    while len(array):
        res += array.pop()

    return res // length


# print(middle_value([5, 10, 15]))

# 1)Дан list:
li = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

#        - знайти мін число
min_number = min(li)

#        - видалити усі дублікати
no_duplicates_set = set(li)
no_duplicates_list = list(no_duplicates_set)

#        - замінити кожне 4-те значення на 'X'
# no_duplicates_list[3:len(res) - 1:3] = ['x'*len(res)]
#
# no_duplicates_list[:10:2] = ['x']
# print(no_duplicates_list)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while


# 4) переробити це завдання під меню

user_input = int(input(
    '1. Find min number\n'
    '2. Remove same values\n'
    '3. Make every third value = "x"\n'
    '4. Middle value\n'
    '5. Exit\n'
    'Make a choice: '))

if user_input == 1:
    print(min_number)
elif user_input == 2:
    print(no_duplicates_list)
elif user_input == 3:
    print('xx')
elif user_input == 4:
    print(middle_value(no_duplicates_list))
else:
    quit()
