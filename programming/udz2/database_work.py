import sqlite3


class DataBase:

    def add_transport(self, type, brand, model, number, tonnage, length, width, height):
        try:
            connection = sqlite3.connect('transportation.db')

            cursor = connection.cursor()
            print("База данных успешно подключена к SQLite")

            max_id = 0
            for i in self.show_transport():
                if i[0] > max_id:
                    max_id = i[0]
            count = max_id + 1

            cursor.execute("INSERT INTO tTransports VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (count, type, brand, model, number,
                                                                                          tonnage, length, width, height))
            connection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")

    def show_transport(self):
        try:
            connection = sqlite3.connect('transportation.db')

            cursor = connection.cursor()
            print("База данных успешно подключена к SQLite")

            cursor.execute('''SELECT * FROM tTransports''')
            trans = cursor.fetchall()

            connection.commit()

            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")
                return trans

    def show_sort_transport(self):
        """ Отсортированный по грузоподъемности список машин """

        trans = self.show_transport()
        trans.sort(key = lambda x: x[5])
        return trans

    def show_free_transport(self, date):
        set1 = set(self.show_sort_transport())
        set2 = set(self.show_booked_transport(date))
        result_set = set1 - set2
        result = list(result_set)
        return result

    def show_booked_transport(self, date):
        try:
            connection = sqlite3.connect('transportation.db')

            cursor = connection.cursor()
            print("База данных успешно подключена к SQLite")

            cursor.execute('''SELECT * FROM tApplications WHERE date = ?''', (date,))
            apps = cursor.fetchall()
            id_cars = []
            for i in apps:
                id_cars.append(i[9])

            cars = []
            for i in self.show_transport():
                if i[0] in id_cars:
                    cars.append(i)

            connection.commit()

            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")
                return cars

    def show_booked_drivers(self, date):
        try:
            connection = sqlite3.connect('transportation.db')

            cursor = connection.cursor()
            print("База данных успешно подключена к SQLite")

            cursor.execute('''SELECT * FROM tApplications WHERE date = ?''', (date,))
            apps = cursor.fetchall()
            id_drivers = []
            for i in apps:
                id_drivers.append(i[10])

            drivers = []
            for i in self.show_driver():
                if i in id_drivers:
                    drivers.append(i)

            connection.commit()

            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")
                return drivers

    def show_free_drivers(self, date):
        set1 = set(self.show_driver())
        set2 = set(self.show_booked_drivers(date))
        result_set = set1 - set2
        result = list(result_set)
        return result

    def show_driver(self):
        try:
            connection = sqlite3.connect('transportation.db')

            cursor = connection.cursor()
            print("База данных успешно подключена к SQLite")

            cursor.execute('''SELECT * FROM tDrivers''')
            dris = cursor.fetchall()

            connection.commit()

            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")
                return dris

    def add_application(self, customer_name, contact_name, contacts, cargo_tonnage, cargo_length, cargo_width,
                        cargo_height, date, idTransport, idDriver):
        try:
            connection = sqlite3.connect('transportation.db')

            cursor = connection.cursor()
            print("База данных успешно подключена к SQLite")

            cursor.execute('''SELECT COUNT(*) FROM tApplications''')
            count = cursor.fetchone()[0] + 1

            cursor.execute("INSERT INTO tApplications VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (count, customer_name, contact_name, contacts,
                                                                                                  cargo_tonnage, cargo_length, cargo_width,
                                                                                                  cargo_height, date, idTransport, idDriver))
            connection.commit()

            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")

    def delete_transport(self, id_transport):
        try:
            connection = sqlite3.connect('transportation.db')

            cursor = connection.cursor()
            print("База данных успешно подключена к SQLite")

            cursor.execute('''DELETE FROM tTransports WHERE id = ?''', (id_transport,))
            connection.commit()

            cursor.close()
        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)
        finally:
            if (connection):
                connection.commit()
                connection.close()
                print("Соединение с SQLite закрыто")

    def show_suitable_transport(self, weight, length, width, height, date):
        trans = self.show_free_transport(date)
        suit_trans = []
        for i in trans:
            if i[5] >= weight and i[6] > length and i[7] > width and i[8] > height:
                suit_trans.append(i)
        return suit_trans


#  print(DataBase().show_booked_transport('23.05.2023'))
