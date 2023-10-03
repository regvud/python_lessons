# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва
# записувати не потрібно)

# try:
#     with open('emails.txt') as efile:
#         emails = efile.read().split()
#     with open('gmails.txt', 'w') as gfile:
#         for email in emails:
#             if email.endswith('@gmail.com'):
#                 gfile.write(f'{email}\n')
# except Exception as err:
#     print(err)

# 2) Створити записну книжку покупок: - у покупки повинна бути id, назва і ціна - всі покупки зберігаємо в файлі з
# функціоналу: * вивід всіх покупок * має бути змога додавати покупку в книгу * має бути змога шукати по будь якому
# полю покупку * має бути змога показати найдорожчу покупку * має бути можливість видаляти покупку по id (ну і меню
# на це все)

from typing import TypedDict
import json


class Purchase(TypedDict):
    id: int
    name: str
    price: int


class BuyBook:
    def __init__(self):
        self.__data: list[Purchase] = []
        self.__read_file()

    @staticmethod
    def __input_int(msg: str) -> int:
        while True:
            ans = input(msg)

            if not ans.isdigit():
                continue

            return int(ans)

    def __read_file(self):
        try:
            with open('buy-book.json', 'r') as file:
                self.__data = json.load(file)
        except (Exception,):
            pass

    def __write_file(self):
        try:
            with open('buy-book.json', 'w') as file:
                json.dump(self.__data, file)
        except (Exception,):
            pass

    def __add(self):
        input_name = input('What do you want to buy?: ')
        input_price = self.__input_int('How much is it?: ')
        pk = self.__data[-1]['id'] + 1 if self.__data else 1

        purchase = Purchase(id=pk, name=input_name, price=input_price)
        self.__data.append(purchase)
        self.__write_file()

    def __show_items(self):
        for i, v in enumerate(self.__data, start=1):
            print(f'{i}) {v}')

    def __search(self):
        search = input('What to search: ')
        for purchase in self.__data:
            for search_value in purchase.keys() | purchase.values():
                if search_value == search:
                    print(purchase)

    def __delete(self):
        self.__show_items()

        pk = self.__input_int('Item id to delete: ')
        index = next((i for i, v in enumerate(self.__data) if v['id'] == pk), None)

        if index is None:
            print('Incorrect index')
            return

        del self.__data[index]
        self.__write_file()

    def __most_expensive(self):
        # most_expensive = list(filter(lambda x: x['price'], self.__data))
        # print(f'RESULT: {most_expensive[-1]}')
        sorted_data = sorted(self.__data, key=lambda i: i['price'])
        print(f'RESULT: {sorted_data[-1]}')

    def menu(self):
        while True:
            print('\nOptions')
            print('1. Add')
            print('2. Show items')
            print('3. Search')
            print('4. Most expensive item')
            print('5. Delete by Id')

            option = input('\nChoose option: ')

            match option:
                case '1':
                    self.__add()
                case '2':
                    self.__show_items()
                case '3':
                    self.__search()
                case '4':
                    self.__most_expensive()
                case '5':
                    self.__delete()


# book = BuyBook()
# book.menu()


# потрібно брати по черзі с кожного списку id і класти в список res, якщо таке значення вже є в результуючому списку
# то брати наступне з того ж підсписку
#
# з даним списком мае вийти ось такий результат:
# res = [1110, 1120, 1130, 1111, 1122, .......]
data = [
    [
        {"id": 1110, "field": {}},
        {"id": 1111, "field": {}},
        {"id": 1112, "field": {}},
        {"id": 1113, "field": {}},
        {"id": 1114, "field": {}},
        {"id": 1115, "field": {}},
    ],
    [
        {"id": 1110, "field": {}},
        {"id": 1120, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1123, "field": {}},
        {"id": 1124, "field": {}},
        {"id": 1125, "field": {}},

    ],
    [
        {"id": 1130, "field": {}},
        {"id": 1131, "field": {}},
        {"id": 1122, "field": {}},
        {"id": 1132, "field": {}},
        {"id": 1133, "field": {}},

    ]
]


def gen(n):
    for i in data[n]:
        yield i


gen_list: list[gen] = []
res = []

for generator in range(len(data)):
    gen_list.append(gen(generator))


while gen_list:
    generator = gen_list.pop(0)

    try:
        item = next(generator)
        if item['id'] not in res:
            res.append(item['id'])
            gen_list.append(generator)
        else:
            next_item = next(generator)
            if next_item['id'] not in res:
                res.append(next_item['id'])
                gen_list.append(generator)
    except StopIteration:
        pass

for obj in res:
    print(obj)
