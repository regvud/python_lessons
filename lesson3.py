# Створити клас Rectangle:
class Rectangle:

    # -він має приймати дві сторони x,y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # при виклику метода len() підраховувати сумму сторін
    def len(self):
        return (self.x + self.y) * 2

    # -описати поведінку на арифметични методи:

    # + сумма площин двох екземплярів ксласу
    def __add__(self, other):
        return (self.x + self.y) * 2 + (other.x + other.y) * 2

    # - різниця площин двох екземплярів ксласу

    def __sub__(self, other):
        return (self.x + self.y) * 2 - (other.x + other.y) * 2
        # return abs((self.x + self.y) * 2 - (other.x + other.y) * 2)

    # == площин на рівність
    def __eq__(self, other):
        return (self.x + self.y) * 2 == (other.x + other.y) * 2

    # != площин на не рівність
    def __ne__(self, other):
        return (self.x + self.y) * 2 != (other.x + other.y) * 2

    # >, < меньше більше
    def __lt__(self, other):
        return (self.x + self.y) * 2 < (other.x + other.y) * 2

    def __gt__(self, other):
        return (self.x + self.y) * 2 > (other.x + other.y) * 2


rec1 = Rectangle(5, 5)
rec2 = Rectangle(10, 5)

print(rec1 < rec2)


# ###############################################################################
# створити класс Human (name, age)

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# створити два класси Prince и Cinderella які наслідуються від Human: у принца має бути ім'я, вік, та розмір
# знайденого черевичка


class Cinderella(Human):
    # в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
    count = 0

    # у попелюшки мае бути ім'я, вік, розмір нонги
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.count += 1

    # також має бути метод классу який буде виводити це значення
    @classmethod
    def show_count(cls):
        print(cls.count)


class Prince(Human):

    def __init__(self, name, age, shoe):
        super().__init__(name, age)
        self.shoe = shoe

    # також метод котрий буде приймати список попелюшок, та шукати ту саму
    def find_shoe(self, arr: list[Cinderella]):
        for i in arr:
            if i.shoe_size == self.shoe:
                print(f'{i.name} + {self.name}')


prince = Prince('Ruslan', 20, 36)

cinderella = Cinderella('Alina', 17, 36)
cinderella2 = Cinderella('Bogdana', 20, 37)
cinderella3 = Cinderella('Larisa', 40, 36)

prince.find_shoe([cinderella, cinderella2, cinderella3])

# ###############################################################################
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()

from abc import ABC, abstractmethod


class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


# 2) Створити класи Book та
# Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
class Book(Printable):

    def __init__(self, name):
        self.name = name

    def print(self):
        pass


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        pass


# 3) Створити клас Main в
# якому буде: - змінна класу printable_list яка буде зберігати книжки та журнали - метод add за допомогою якого можна
# додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше
# ігрнорувати додавання

# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()

# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False

class Main(Printable):
    printable_list: list[Book, Magazine] = []

    def print(self):
        pass

    @classmethod
    def add(cls, item):
        if isinstance(item, Book | Magazine):
            cls.printable_list.append(item)
        else:
            print('Item is not book or magazine')

    @classmethod
    def show_all_magazines(cls):
        magazines: list[Magazine] = [i.name for i in cls.printable_list if isinstance(i, Magazine)]
        return magazines

    @classmethod
    def show_all_books(cls):
        books: list[Book] = [i.name for i in cls.printable_list if isinstance(i, Book)]
        return books


Main.add(Book('GOT'))
Main.add(Book('Standy'))
Main.add(Book('Harry Potter'))

Main.add(Magazine('Love'))
Main.add(Magazine('War'))
Main.add(Magazine('Crime'))

print(Main.show_all_magazines())
print(Main.show_all_books())
