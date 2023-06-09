class Counting(object):
    """ class for counting objects """

    i = 0

    def __init__(self):
        self.__class__.i += 1
        self.c = self.__class__.i

    def get_number(self):
        print(f'Мой порядковый номер: {self.c}')


def main():
    o1 = Counting()
    o2 = Counting()
    o3 = Counting()
    o1.get_number()
    o3.get_number()
    o2.get_number()


main()
