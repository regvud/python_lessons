# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли з доменом gmail.com (Хеш то що з ліва
# записувати не потрібно)

# try:
#     with open('emails.txt') as file:
#         emails = file.read().split()
# except Exception as err:
#     print(err)
#
# try:
#     with open('gmails.txt', 'w') as file:
#         for email in emails:
#             if email.endswith('@gmail.com'):
#                 file.write(f'{email}\n')
# except Exception as err:
#     print(err)


# 2) Створити записну книжку покупок: - у покупки повинна бути id, назва і ціна - всі покупки зберігаємо в файлі з
# функціоналу: * вивід всіх покупок * має бути змога додавати покупку в книгу * має бути змога шукати по будь якому
# полю покупку * має бути змога показати найдорожчу покупку * має бути можливість видаляти покупку по id (ну і меню
# на це все)


class Purchase:
    id = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Purchase.id += 1

    def __repr__(self):
        return f'name: {self.name}, price: {self.price}, id: {self.id}'


buy_book = []

while True:
    init_input = input('Choose option: ')

    match init_input:
        case '1':
            input_name = input('What do you want to buy?: ')
            input_price = int(input('How much is it?: '))

            purchase = Purchase(input_name, input_price)
            buy_book.append(purchase)

            try:
                with open('buy-book.txt', 'w+') as file:
                    for buy in buy_book:
                        file.write(f'{buy}\n')
            except Exception as err:
                print(err)

        case '2':
            pass