class Customer:
    """ class for customer of telephone company """

    def __init__(self, name, tariff, balance=0):
        self.name = name
        self.balance = balance
        self.tariff = tariff

    def record_payment(self, add):
        self.balance += add

#    def record_call(self, call_type, minutes):
#        pay = 0
#        if call_type == 1:
#            pay = minutes * 5
#        elif call_type == 2:
#            pay = minutes
#        self.record_payment(-pay)

    def record_call(self, call_type, minutes):
        pay = self.tariff.payment(call_type, minutes)
        self.record_payment(-pay)


class Tariff:
    """ Базовый класс для тарифов """
    def payment(self, call_type, minutes):
        pass


class TimeTariff(Tariff):

    def payment(self, call_type, minutes):
        super().payment(call_type, minutes)
        pay = 0
        if call_type == 1:
            pay = minutes * 5
        elif call_type == 2:
            pay = minutes
        return pay


class Minutes10Tariff(Tariff):

    def payment(self, call_type, minutes):
        super().payment(call_type, minutes)
        pay = 0
        if call_type == 1:
            pay = minutes * 5
            if minutes > 10:
                pay -= (minutes - 10)*2.5
        elif call_type == 2:
            pay = minutes
            if minutes > 10:
                pay -= (minutes - 10)*0.5
        return pay


class Minutes5Tariff(Tariff):

    def payment(self, call_type, minutes):
        super().payment(call_type, minutes)
        pay = 0
        if minutes > 5:
            if call_type == 1:
                pay = 5 * 2.5 + (minutes - 5) * 10
            elif call_type == 2:
                pay = 5 * 0.5 + (minutes - 5) * 2
        elif minutes <= 5:
            if call_type == 1:
                pay = minutes * 2.5
            elif call_type == 2:
                pay = minutes * 0.5
        return pay


def main():
    print('Приветствуем в нашей телефонной компании!')
    name = input('Введите своё имя: ')
    print('Мы предлагаем Вам на выбор три тарифа: 1 - Повременный; 2 - После 10 минут в 2 раза дешевле; 3 - Плати меньше до 5 минут: ')
    t_num = input('Введите номер желаемого тарифа: ')
    if t_num == '1':
        tariff = TimeTariff()
    elif t_num == '2':
        tariff = Minutes10Tariff()
    elif t_num == '3':
        tariff = Minutes5Tariff()
    client1 = Customer(name, tariff)

    answer = '0'
    while answer != '4':
        answer = input('Что хотите сделать? 1 - совершить звонок; 2 - пополнить баланс; 3 - посмотреть баланс; 4 - выйти: ')
        if answer == '1':
            call_type = input('Какой тип звонка совершен? 1 - городской; 2 - мобильный: ')
            minutes = input('Сколько минут длился разговор?: ')
            client1.record_call(int(call_type), int(minutes))
        elif answer == '2':
            money = input('На сколько рублей вы хотите пополнить баланс?: ')
            client1.record_payment(float(money))
        elif answer == '3':
            print(f'Ваш текущий баланс составляет: {client1.balance}')
    print(f'Всего доброго, {client1.name}!')


main()
