class Publication:
    """ class for publication """

    def __init__(self, name='', price=0):
        self.name = name
        self.price = price

    def get_data(self):
        self.name = input('Введите название книги: ')
        self.price = input('Введите стоимость книги: ')

    def put_data(self):
        print(f'Название книги: {self.name}')
        print(f'Стоимость книги: {self.price}')


class Book(Publication):
    """ class for paper book """

    def __init__(self, name='', price=0, papers=0):
        super().__init__(name, price)
        self.papers = papers

    def get_data(self):
        super().get_data()
        self.papers = input('Введите количество страниц: ')

    def put_data(self):
        super().put_data()
        print(f'Количество страниц: {self.papers}')


class AudioBook(Publication):
    """ class for audio-book """

    def __init__(self, name='', price=0, minutes=0):
        super().__init__(name, price)
        self.minutes = minutes

    def get_data(self):
        super().get_data()
        self.minutes = input('Введите время записи книги в минутах: ')

    def put_data(self):
        super().put_data()
        print(f'Количество минут записи: {self.minutes}')


def main():
    book1 = Book()
    book2 = AudioBook()
    book1.get_data()
    book2.get_data()
    book1.put_data()
    book2.put_data()


main()
