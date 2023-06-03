class Employee:
    """ class for employee information """

    def __init__(self):
        self.fee = 0
        self.number = 0

    def set_number(self, number):
        self.number = number

    def set_fee(self, fee):
        self.fee = fee

    def get_number(self):
        return self.number

    def get_fee(self):
        return self.fee


def work():
    num = input('Введите номер сотрудника: ')
    fee = input('Введите оклад сотрудника: ')
    em = Employee()
    em.set_number(num)
    em.set_fee(fee)
    print(f'Номер сотрудника: {em.get_number()}, оклад сотрудника: {em.get_fee()}')


work()
