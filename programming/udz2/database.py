import sqlite3

try:
    connection = sqlite3.connect('transportation.db')

    cursor = connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    cursor.execute('''CREATE TABLE tTransports(id INTEGER PRIMARY KEY, type TEXT, brand TEXT, model TEXT, number TEXT, 
                      tonnage REAL, length REAL, width REAL, height REAL)''')
    connection.commit()

    cursor.execute('''CREATE TABLE tDrivers(id INTEGER PRIMARY KEY, surname TEXT, name TEXT, father_name TEXT, experience INTEGER)''')
    connection.commit()

    cursor.execute('''CREATE TABLE tApplications(id INTEGER PRIMARY KEY, customer_name TEXT, contact_name TEXT, contacts TEXT, 
                      cargo_tonnage REAL, cargo_length REAL, cargo_width REAL, cargo_height REAL, date TEXT, idTransport INTEGER,
                      idDriver INTEGER, FOREIGN KEY(idTransport) REFERENCES tTransports(id), FOREIGN KEY(idDriver) REFERENCES tDrivers(id))''')
    connection.commit()

    # TODO: Реализовать бронирование транспорта (таблица Бронь)

    data_t = [(1, 'Газель', 'ГАЗ', 'Next', 'о812мм', 2, 3, 2, 2.2), (2, 'Фургон', 'Ford', 'Transit', 'к765ас', 2.2, 3, 2, 2.3),
              (3, 'Бычок', 'ЗИЛ', '5301', 'р529та', 3, 4.5, 2.2, 2.4), (4, 'Грузовик', 'MAN', '10', 'р664кс', 10, 8, 2.45, 2.5),
              (5, 'Фура', 'Mercedes-Benz', 'Actros', 'е902ув', 20, 13.6, 2.46, 2.7)]
    cursor.executemany("INSERT INTO tTransports VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", data_t)
    connection.commit()

    data_d = [(1, 'Боженко', 'Мария', 'Александровна', 2), (2, 'Оншин', 'Дмитрий', 'Николаевич', 1), (3, 'Надери', 'Мариам', 'Шаховна', 12),
              (4, 'Миляев', 'Дмитрий', 'Дмитриевич', 1), (5, 'Адрат', 'Олеся', 'Александровна', 10), (6, 'Шишминцев', 'Дмитрий', 'Владимирович', 24),
              (7, 'Петрова', 'Наталья', 'Глебовна', 1), (8, 'Агаев', 'Хамза', 'Рустам Оглы', 16)]
    cursor.executemany("INSERT INTO tDrivers VALUES (?, ?, ?, ?, ?)", data_d)
    connection.commit()

    data_a = [(1, 'Петров Арылхан Владимирович', 'Петров Арылхан Владимирович', '89217689383', 2, 1.5, 1, 1, '22.05.2023', 2, 4),
              (2, 'ООО Цветочек', 'Федоров Владислав Дмитриевич', '89217689383', 15, 10, 2, 2, '23.05.2023', 5, 8)]
    cursor.executemany("INSERT INTO tApplications VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data_a)
    connection.commit()

    cursor.execute('''SELECT * FROM tDrivers WHERE experience > ?''', (1,))
    print(cursor.fetchone())

    cursor.execute('''SELECT * FROM tApplications''')
    res = cursor.fetchall()[1][9]

    cursor.execute('''SELECT * FROM tTransports WHERE id = ?''', (res,))
    print(cursor.fetchall())

    mas = [2, 4, 7]
    for i in mas:
        cursor.execute('''SELECT * FROM tDrivers WHERE id = ?''', (i,))
        print(cursor.fetchall())

    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")
