from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.messagebox import showinfo, showerror, askyesno
from exceptions import *
from database_work import *


class Window(Frame):

    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)

        container = Frame(self)
        container.pack(side='right', fill='both', expand=True)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        buttonframe = Frame(self)
        buttonframe.pack()

        self.bt_add = Button(buttonframe, text='Добавить ТС', bg='white', command=p1.show_page, width=20, height=6)
        self.bt_add.pack(padx=5, pady=5)
        self.bt_delete = Button(buttonframe, text='Удалить ТС', bg='white', command=p2.show_page, width=20, height=6)
        self.bt_delete.pack(padx=5, pady=5)
        self.bt_search = Button(buttonframe, text='Поиск ТС', bg='white', command=p3.show_page, width=20, height=6)
        self.bt_search.pack(padx=5, pady=5)
        self.bt_app = Button(buttonframe, text='Подать заявку', bg='white', command=p4.show_page, width=20, height=6)
        self.bt_app.pack(padx=5, pady=5)
        self.bt_find = Button(buttonframe, text='Подобрать ТС', bg='white', command=p5.show_page, width=20, height=6)
        self.bt_find.pack(padx=5, pady=5)
        p1.show_page()


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show_page(self):
        self.lift()
        self.update_data()

    def help_me(self):
        help_root = Tk()
        help_root['bg'] = '#fafafa'  # background
        help_root.title('Справка')  # title of window
        help_root.geometry('900x120')  # size of the window
        help_root.resizable(width=False, height=False)  # user can't change size of the window

        help_root.iconbitmap('help.ico')

        Label(help_root, text='Это программа \"ЛогиСтатик\", предназначенная для контроля траспортного средства и перевозок грузов.',
              bg='#fafafa').place(x=5, y=5)
        Label(help_root, text='Для выбора одного из режимов, нажмите на одну из кнопок слева.', bg='#fafafa').place(x=5, y=25)
        Label(help_root, text='Не пытайтесь вводить некорректные значения. Например, записывать буквы в полях, '
                              'предназначенных для числовых значений', bg='#fafafa').place(x=5, y=45)

    def update_data(self):
        pass


class Page1(Page):
    """ Добавление Траснпортного средства """

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.frame0 = Frame(self)
        self.frame0.pack(fill='x')

        self.label_brand = Label(self.frame0, text='Добавление Транспортного средства в базу данных', font=35)
        self.label_brand.pack(fill='x', padx=5, pady=10, expand=True)

        self.frame1 = Frame(self)
        self.frame1.pack(fill='x', padx=30)

        self.label_type = Label(self.frame1, text='Тип ТС', width=30, anchor='e')
        self.label_type.pack(side='left', padx=5, pady=5)
        self.arg_type = Entry(self.frame1, justify=LEFT, width=30)
        self.arg_type.pack(side='left', padx=10)

        self.frame2 = Frame(self)
        self.frame2.pack(fill='x', padx=30)

        self.label_brand = Label(self.frame2, text='Марка ТС', width=30, anchor='e')
        self.label_brand.pack(side='left', padx=5, pady=5)
        self.arg_brand = Entry(self.frame2, justify=LEFT, width=30)
        self.arg_brand.pack(side='left', padx=10)

        self.frame3 = Frame(self)
        self.frame3.pack(fill='x', padx=30)

        self.label_model = Label(self.frame3, text='Модель', width=30, anchor='e')
        self.label_model.pack(side='left', padx=5, pady=5)
        self.arg_model = Entry(self.frame3, justify=LEFT, width=30)
        self.arg_model.pack(side='left', padx=10)

        self.frame4 = Frame(self)
        self.frame4.pack(fill='x', padx=30)

        self.label_number = Label(self.frame4, text='Номер ТС', width=30, anchor='e')
        self.label_number.pack(side='left', padx=5, pady=5)
        self.arg_number = Entry(self.frame4, justify=LEFT, width=30)
        self.arg_number.pack(side='left', padx=10)

        self.frame5 = Frame(self)
        self.frame5.pack(fill='x', padx=30)

        self.label_tonnage = Label(self.frame5, text='Грузоподъемность', width=30, anchor='e')
        self.label_tonnage.pack(side='left', padx=5, pady=5)
        self.arg_tonnage = Entry(self.frame5, justify=LEFT, width=30)
        self.arg_tonnage.pack(side='left', padx=10)

        self.frame6 = Frame(self)
        self.frame6.pack(fill='x', padx=30)

        self.label_length = Label(self.frame6, text='Длина', width=30, anchor='e')
        self.label_length.pack(side='left', padx=5, pady=5)
        self.arg_length = Entry(self.frame6, justify=LEFT, width=30)
        self.arg_length.pack(side='left', padx=10)

        self.frame7 = Frame(self)
        self.frame7.pack(fill='x', padx=30)

        self.label_width = Label(self.frame7, text='Ширина', width=30, anchor='e')
        self.label_width.pack(side='left', padx=5, pady=5)
        self.arg_width = Entry(self.frame7, justify=LEFT, width=30)
        self.arg_width.pack(side='left', padx=10)

        self.frame8 = Frame(self)
        self.frame8.pack(fill='x', padx=30)

        self.label_height = Label(self.frame8, text='Высота', width=30, anchor='e')
        self.label_height.pack(side='left', padx=5, pady=5)
        self.arg_height = Entry(self.frame8, justify=LEFT, width=30)
        self.arg_height.pack(side='left', padx=10)

        self.frame9 = Frame(self)
        self.frame9.pack(fill='x', padx=30)

        self.add_btn = Button(self.frame9, text='Добавить', width=15, command=self.action)
        self.add_btn.pack(side='right', padx=20, pady=10)
        self.clear_btn = Button(self.frame9, text='Очистить', width=15, command=self.clear)
        self.clear_btn.pack(side='right', padx=20, pady=10)

    def action(self):
        mas_args = [self.arg_type, self.arg_brand, self.arg_model, self.arg_number, self.arg_tonnage,
                    self.arg_length, self.arg_width, self.arg_height]
        symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
        letters = ['у', 'к', 'е', 'н', 'х', 'в', 'а', 'р', 'о', 'с', 'м', 'т']

        try:
            for i in mas_args:
                if not i.get():
                    raise EmptyEnter
            for i in self.arg_tonnage.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_length.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_width.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_height.get():
                if i not in symbols:
                    raise NoDigitsError
            num = self.arg_number.get()
            if num[0] not in letters or not num[1].isdigit() or not num[2].isdigit() or not num[3].isdigit() or num[4] not in letters or num[5] not in letters or len(num) != 6:
                raise IncorrectCarNumber
            DataBase().add_transport(self.arg_type.get(), self.arg_brand.get(), self.arg_model.get(), self.arg_number.get(), float(self.arg_tonnage.get()),
                                     float(self.arg_length.get()), float(self.arg_width.get()), float(self.arg_height.get()))
            showinfo(title='Информация', message=f'Было добавлено новое Транспортное средство: {self.arg_brand.get()} {self.arg_model.get()} {self.arg_number.get()}')
            self.clear()
        except EmptyEnter:
            showerror(title='Ошибка', message='Заполните, пожалуйста, все поля!')
        except NoDigitsError:
            showerror(title='Ошибка', message='Будьте внимательны! В некоторых полях должны быть введены числовые значения!')
        except IncorrectCarNumber:
            showerror(title='Ошибка', message='Введите номер ТС в следующем формате: \"о111оо\", где о - одна из букв: у, к, е, н, х, в, а, р, о, с, м, т; а 0 - цифра.')

    def clear(self):
        self.arg_number.delete(0, END)
        self.arg_model.delete(0, END)
        self.arg_brand.delete(0, END)
        self.arg_length.delete(0, END)
        self.arg_tonnage.delete(0, END)
        self.arg_height.delete(0, END)
        self.arg_width.delete(0, END)
        self.arg_type.delete(0, END)

    def update_data(self):
        self.clear()


class Page2(Page):
    """ Удаление Транпортного средства """

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        self.cars = DataBase().show_transport()
        self.cars_text = []  # список со строками (1 строка - информация по машине)
        for i in self.cars:
            self.cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')

        self.frame0 = Frame(self)
        self.frame0.pack(fill='x')

        self.label_brand = Label(self.frame0, text='Удаление Транспортного средства из базы данных', font=35)
        self.label_brand.pack(fill='x', padx=5, pady=10, expand=True)

        self.var = StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.var, width=30)
        self.combobox['values'] = self.cars_text
        self.combobox['state'] = 'readonly'
        self.combobox.pack(side='top', fill='x', pady=10, padx=30)
        self.combobox.bind("<<ComboboxSelected>>", self.selected)

        self.frame1 = Frame(self)
        self.frame1.pack(fill='x', padx=30)

        self.del_btn = Button(self.frame1, text='Удалить', width=15, state='disabled', command=self.action)
        self.del_btn.pack(side='right', padx=20, pady=10)
        self.clear_btn = Button(self.frame1, text='Очистить', width=15, command=self.clear)
        self.clear_btn.pack(side='right', padx=20, pady=10)

    def action(self):
        current_transport = self.var.get()
        id_transport = current_transport.split('.')[0]
        answer = askyesno(title='Предупреждение', message=f'Вы уверены, что хотите удалить транспорт {current_transport}?')
        if answer:
            DataBase().delete_transport(int(id_transport))
            showinfo(title='Информация', message=f'Было удалено Транспортное средство: {current_transport}')
            self.update_data()

    def selected(self, event):
        selection = self.combobox.get()
        if selection != '':
            self.del_btn['state'] = 'normal'

    def clear(self):
        self.combobox.set('')
        self.del_btn['state'] = 'disabled'

    def update_data(self):
        self.clear()
        self.cars = DataBase().show_transport()  # Обновление содержимого в combobox
        self.cars_text = []
        for i in self.cars:
            self.cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')
        self.combobox['values'] = self.cars_text


class Page3(Page):
    """ Поиск Транспортного средства """

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        cars = DataBase().show_transport()
        cars_text = []  # список со строками (1 строка - информация по машине)
        for i in cars:
            cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')

        self.frame0 = Frame(self)
        self.frame0.pack(fill='x')

        self.label_brand = Label(self.frame0, text='Поиск Транспортного средства в базе данных', font=35)
        self.label_brand.pack(fill='x', padx=5, pady=10, expand=True)

        self.frame1 = Frame(self)
        self.frame1.pack(fill='x')

        self.pos = StringVar(value='nosort')
        self.nosort_btn = Radiobutton(self.frame1, text='Без сортировки', variable=self.pos, value='nosort', command = lambda : self.update_data())
        self.nosort_btn.pack(padx=30, pady=5, side='left')
        self.tonnage_btn = Radiobutton(self.frame1, text='По грузоподъемности', variable=self.pos, value='tonnage', command = lambda : self.tonnage())
        self.tonnage_btn.pack(padx=5, pady=5, side='left')
        self.book_btn = Radiobutton(self.frame1, text='По бронированию', variable=self.pos, value='free', command = lambda : self.bron())
        self.book_btn.pack(padx=5, pady=5, side='left')

        self.var = StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.var, width=30)
        self.combobox['values'] = cars_text
        self.combobox['state'] = 'readonly'
        self.combobox.pack(side='top', fill='x', pady=10, padx=30)

        self.frame3 = Frame(self)
        self.frame3.pack(fill='x')

        self.label_bron = Label(self.frame3, text='Вывести ТС', width=30, anchor='e')
        self.label_bron.pack(side='left', padx=5, pady=5)
        self.pos_bron = StringVar(value='book')
        self.booked_btn = Radiobutton(self.frame3, text='забронированные', variable=self.pos_bron, value='book',
                                      state='disabled', command=lambda: self.selected_date("<<CalendarSelected>>"))
        self.booked_btn.pack(padx=5, pady=5, side='left')
        self.free_btn = Radiobutton(self.frame3, text='свободные', variable=self.pos_bron, value='free',
                                    state='disabled', command=lambda: self.selected_date("<<CalendarSelected>>"))
        self.free_btn.pack(padx=5, pady=5, side='left')

        self.frame4 = Frame(self)
        self.frame4.pack(fill='x')

        self.cal = Calendar(self.frame4, selectmode='day', year=2023, month=1, day=1, state='disabled', date_pattern="dd.mm.yyyy")
        self.cal.pack(side='top', padx=10)
        self.cal.bind("<<CalendarSelected>>", self.selected_date)

        free_cars = DataBase().show_booked_transport(str(self.cal.get_date()))
        free_cars_text = []  # список со строками (1 строка - информация по машине)
        for i in free_cars:
            free_cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')

        self.var2 = StringVar()
        self.combobox2 = ttk.Combobox(self, textvariable=self.var2, width=30, state='disabled')
        self.combobox2['values'] = free_cars_text
        self.combobox2['state'] = 'readonly'
        self.combobox2.pack(side='top', fill='x', pady=10, padx=30)

    def selected_date(self, event):
        if self.pos_bron.get() == 'book':
            free_cars = DataBase().show_booked_transport(str(self.cal.get_date()))
        elif self.pos_bron.get() == 'free':
            free_cars = DataBase().show_free_transport(str(self.cal.get_date()))
        free_cars_text = []  # список со строками (1 строка - информация по машине)
        for i in free_cars:
            free_cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')
        self.combobox2['values'] = free_cars_text

    def bron(self):
        self.combobox['state'] = 'disabled'
        self.booked_btn['state'] = 'normal'
        self.free_btn['state'] = 'normal'
        self.cal['state'] = 'normal'
        self.combobox2['state'] = 'normal'

    def tonnage(self):
        self.combobox['state'] = 'normal'
        sort_cars = DataBase().show_sort_transport()
        cars_text = []  # список со строками (1 строка - информация по машине)
        for i in sort_cars:
            cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')
        self.combobox['values'] = cars_text
        self.booked_btn['state'] = 'disabled'
        self.free_btn['state'] = 'disabled'
        self.cal['state'] = 'disabled'
        self.combobox2['state'] = 'disabled'

    def update_data(self):
        self.clear()
        self.cars = DataBase().show_transport()  # Обновление содержимого в combobox
        self.cars_text = []
        for i in self.cars:
            self.cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')
        self.combobox['values'] = self.cars_text
        self.combobox['state'] = 'normal'
        self.booked_btn['state'] = 'disabled'
        self.free_btn['state'] = 'disabled'
        self.cal['state'] = 'disabled'
        self.combobox2['state'] = 'disabled'

    def clear(self):
        self.combobox.set('')

    def booked(self):
        pass


class Page4(Page):
    """ Подача заявки """

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.frame0 = Frame(self)
        self.frame0.pack(fill='x')

        self.label_page = Label(self.frame0, text='Подача заявки на первозку груза', font=35)
        self.label_page.pack(fill='x', padx=5, pady=10, expand=True)

        self.frame1 = Frame(self)
        self.frame1.pack(fill='x', padx=30)

        self.label_customer = Label(self.frame1, text='Заказчик', width=30, anchor='e')
        self.label_customer.pack(side='left', padx=5, pady=5)
        self.arg_customer = Entry(self.frame1, justify=LEFT, width=30)
        self.arg_customer.pack(side='left', padx=10)

        self.frame2 = Frame(self)
        self.frame2.pack(fill='x', padx=30)

        self.label_contact_name = Label(self.frame2, text='Контактное лицо', width=30, anchor='e')
        self.label_contact_name.pack(side='left', padx=5, pady=5)
        self.arg_contact_name = Entry(self.frame2, justify=LEFT, width=30)
        self.arg_contact_name.pack(side='left', padx=10)

        self.frame3 = Frame(self)
        self.frame3.pack(fill='x', padx=30)

        self.label_contacts = Label(self.frame3, text='Контакты', width=30, anchor='e')
        self.label_contacts.pack(side='left', padx=5, pady=5)
        self.arg_contacts = Entry(self.frame3, justify=LEFT, width=30)
        self.arg_contacts.pack(side='left', padx=10)

        self.frame31 = Frame(self)
        self.frame31.pack(fill='x', padx=30)

        self.label_weight = Label(self.frame31, text='Вес груза', width=30, anchor='e')
        self.label_weight.pack(side='left', padx=5, pady=5)
        self.arg_weight = Entry(self.frame31, justify=LEFT, width=30)
        self.arg_weight.pack(side='left', padx=10)

        self.frame4 = Frame(self)
        self.frame4.pack(fill='x', padx=30)

        self.label_height = Label(self.frame4, text='Высота груза', width=30, anchor='e')
        self.label_height.pack(side='left', padx=5, pady=5)
        self.arg_height = Entry(self.frame4, justify=LEFT, width=30)
        self.arg_height.pack(side='left', padx=10)

        self.frame5 = Frame(self)
        self.frame5.pack(fill='x', padx=30)

        self.label_width = Label(self.frame5, text='Ширина груза', width=30, anchor='e')
        self.label_width.pack(side='left', padx=5, pady=5)
        self.arg_width = Entry(self.frame5, justify=LEFT, width=30)
        self.arg_width.pack(side='left', padx=10)

        self.frame6 = Frame(self)
        self.frame6.pack(fill='x', padx=30)

        self.label_length = Label(self.frame6, text='Длина груза', width=30, anchor='e')
        self.label_length.pack(side='left', padx=5, pady=5)
        self.arg_length = Entry(self.frame6, justify=LEFT, width=30)
        self.arg_length.pack(side='left', padx=10)

        self.frame61 = Frame(self)
        self.frame61.pack(fill='x', padx=30)

        self.add_btn = Button(self.frame61, text='Утвердить', width=15, command=self.utv)
        self.add_btn.pack(side='right', padx=20, pady=5)
        self.clear_btn = Button(self.frame61, text='Очистить', width=15, command=self.clear)
        self.clear_btn.pack(side='right', padx=20, pady=5)

        self.frame7 = Frame(self)
        self.frame7.pack(fill='x', padx=30)

        self.label_date = Label(self.frame7, text='Дата перевозки', width=30, anchor='e', state='disabled')
        self.label_date.pack(side='left', padx=5, pady=5)
        self.cal = Calendar(self.frame7, selectmode='day', year=2023, month=1, day=1, date_pattern="dd.mm.yyyy", state='disabled')
        self.cal.pack(side='left', padx=10)

        self.frame8 = Frame(self)
        self.frame8.pack(fill='x', padx=30)

        self.cars = DataBase().show_free_transport(self.cal.get_date())
        self.cars_text = []  # список со строками (1 строка - информация по машине)
        for i in self.cars:
            self.cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')

        self.label_cars = Label(self.frame8, text='Подходящий транспорт', width=30, anchor='e', state='disabled')
        self.label_cars.pack(side='left', padx=5, pady=5)
        self.var = StringVar()
        self.combobox = ttk.Combobox(self.frame8, textvariable=self.var, width=30, state='disabled')
        self.combobox['values'] = self.cars_text
        self.combobox['state'] = 'readonly'
        self.combobox.pack(side='top', fill='x', pady=5, padx=30)
        self.combobox.bind("<<ComboboxSelected>>", self.selected1)

        self.frame9 = Frame(self)
        self.frame9.pack(fill='x', padx=30)

        self.drivers = DataBase().show_free_drivers(self.cal.get_date())
        self.drivers_text = []  # список со строками (1 строка - информация по машине)
        for i in self.drivers:
            self.drivers_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]}')

        self.label_drivers = Label(self.frame9, text='Свободные водители', width=30, anchor='e', state='disabled')
        self.label_drivers.pack(side='left', padx=5, pady=5)
        self.var = StringVar()
        self.combobox2 = ttk.Combobox(self.frame9, textvariable=self.var, width=30, state='disabled')
        self.combobox2['values'] = self.drivers_text
        self.combobox2['state'] = 'readonly'
        self.combobox2.pack(side='top', fill='x', pady=5, padx=30)
        self.combobox2.bind("<<ComboboxSelected>>", self.selected2)

        self.frame10 = Frame(self)
        self.frame10.pack(fill='x', padx=30)

        self.add_btn = Button(self.frame10, text='Подать заявку', width=15, command=self.action, state='disabled')
        self.add_btn.pack(side='right', padx=20, pady=5)
        self.clear_btn = Button(self.frame10, text='Очистить всё', width=15, command=self.clear, state='disabled')
        self.clear_btn.pack(side='right', padx=20, pady=5)

    def action(self):
        try:
            #TODO: доделать ошибки
            DataBase().add_application(self.arg_customer, self.arg_contact_name, self.arg_contacts, self.arg_weight, self.arg_length,
                                       self.arg_width, self.arg_height, self.cal.get_date(), self.combobox.get().split('.')[0], self.combobox2.get().split('.')[0])
            showinfo(title='Информация', message=f'Была добавлена новая заявка')
            self.clear()
        except EmptyEnter:
            showerror(title='Ошибка', message='Заполните, пожалуйста, все поля!')
        except NoDigitsError:
            showerror(title='Ошибка', message='Будьте внимательны! В некоторых полях должны быть введены числовые значения!')

    def selected1(self, event):
        pass

    def selected2(self, event):
        pass

    def utv(self):
        mas_args = [self.arg_customer, self.arg_contacts, self.arg_contact_name, self.arg_weight,
                    self.arg_length, self.arg_width, self.arg_height]
        symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

        try:
            for i in mas_args:
                if not i.get():
                    raise EmptyEnter
            for i in self.arg_weight.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_length.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_width.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_height.get():
                if i not in symbols:
                    raise NoDigitsError
            self.label_date['state'] = 'normal'
            self.label_cars['state'] = 'normal'
            self.label_drivers['state'] = 'normal'
        except EmptyEnter:
            showerror(title='Ошибка', message='Заполните, пожалуйста, все поля!')
        except NoDigitsError:
            showerror(title='Ошибка', message='Будьте внимательны! В некоторых полях должны быть введены числовые значения!')

    def clear(self):
        self.combobox.set('')

    def update_data(self):
        self.clear()
        self.combobox['state'] = 'disabled'
        self.combobox2['state'] = 'disabled'


class Page5(Page):
    """ Подбор траспортного средства """

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        cars = DataBase().show_transport()
        cars_text = []  # список со строками (1 строка - информация по машине)
        for i in cars:
            cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')

        self.frame0 = Frame(self)
        self.frame0.pack(fill='x')

        self.label_brand = Label(self.frame0, text='Подбор Транспортного средства', font=35)
        self.label_brand.pack(fill='x', padx=5, pady=10, expand=True)

        self.frame1 = Frame(self)
        self.frame1.pack(fill='x', padx=30)

        self.label_weight = Label(self.frame1, text='Вес груза', width=30, anchor='e')
        self.label_weight.pack(side='left', padx=5, pady=5)
        self.arg_weight = Entry(self.frame1, justify=LEFT, width=30)
        self.arg_weight.pack(side='left', padx=10)

        self.frame2 = Frame(self)
        self.frame2.pack(fill='x', padx=30)

        self.label_length = Label(self.frame2, text='Длина', width=30, anchor='e')
        self.label_length.pack(side='left', padx=5, pady=5)
        self.arg_length = Entry(self.frame2, justify=LEFT, width=30)
        self.arg_length.pack(side='left', padx=10)

        self.frame3 = Frame(self)
        self.frame3.pack(fill='x', padx=30)

        self.label_width = Label(self.frame3, text='Ширина', width=30, anchor='e')
        self.label_width.pack(side='left', padx=5, pady=5)
        self.arg_width = Entry(self.frame3, justify=LEFT, width=30)
        self.arg_width.pack(side='left', padx=10)

        self.frame4 = Frame(self)
        self.frame4.pack(fill='x', padx=30)

        self.label_height = Label(self.frame4, text='Высота', width=30, anchor='e')
        self.label_height.pack(side='left', padx=5, pady=5)
        self.arg_height = Entry(self.frame4, justify=LEFT, width=30)
        self.arg_height.pack(side='left', padx=10)

        self.frame5 = Frame(self)
        self.frame5.pack(fill='x', padx=30)

        self.label_date = Label(self.frame5, text='Требуемая дата', width=30, anchor='e')
        self.label_date.pack(side='left', padx=5, pady=5)
        self.cal = Calendar(self.frame5, selectmode='day', year=2023, month=1, day=1, date_pattern="dd.mm.yyyy")
        self.cal.pack(side='left', padx=10)

        self.frame6 = Frame(self)
        self.frame6.pack(fill='x', padx=30)

        self.search_btn = Button(self.frame6, text='Поиск', width=15, command=self.action)
        self.search_btn.pack(side='top', padx=20, pady=10)

        self.frame8 = Frame(self)
        self.frame8.pack(fill='x', padx=30)

        self.cars = DataBase().show_free_transport(self.cal.get_date())
        self.cars_text = []  # список со строками (1 строка - информация по машине)
        for i in self.cars:
            self.cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')

        self.label_cars = Label(self.frame8, text='Подходящий транспорт', width=30, anchor='e')
        self.label_cars.pack(side='left', padx=5, pady=5)
        self.var = StringVar()
        self.combobox = ttk.Combobox(self.frame8, textvariable=self.var, width=30, state='disabled')
        self.combobox['values'] = self.cars_text
        self.combobox['state'] = 'readonly'
        self.combobox.pack(side='top', fill='x', pady=10, padx=30)
        # self.combobox.bind("<<ComboboxSelected>>", self.selected1)

    def action(self):
        mas_args = [self.arg_weight, self.arg_length, self.arg_width, self.arg_height]
        symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

        try:
            for i in mas_args:
                if not i.get():
                    raise EmptyEnter
            for i in self.arg_weight.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_length.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_width.get():
                if i not in symbols:
                    raise NoDigitsError
            for i in self.arg_height.get():
                if i not in symbols:
                    raise NoDigitsError
            self.combobox['state'] = 'normal'

            self.cars = DataBase().show_suitable_transport(float(self.arg_weight.get()), float(self.arg_length.get()),
                                                           float(self.arg_width.get()), float(self.arg_height.get()), self.cal.get_date())
            self.cars_text = []  # список со строками (1 строка - информация по машине)
            for i in self.cars:
                self.cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')

            self.combobox['values'] = self.cars_text
        except EmptyEnter:
            showerror(title='Ошибка', message='Заполните, пожалуйста, все поля!')
        except NoDigitsError:
            showerror(title='Ошибка', message='Будьте внимательны! Во всех полях должны быть введены числовые значения!')

    def clear(self):
        self.arg_length.delete(0, END)
        self.arg_weight.delete(0, END)
        self.arg_height.delete(0, END)
        self.arg_width.delete(0, END)

    def update_data(self):
        self.clear()
        self.combobox['state'] = 'disabled'

if __name__ == "__main__":
    root = Tk()
    main = Window(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x600")
    root.title('ЛогиСтатик')
    root.iconbitmap('truck.ico')
    root.resizable(width=False, height=False)

    mainmenu = Menu(root)
    root.config(menu=mainmenu)
    filemenu = Menu(mainmenu, tearoff=0)
    filemenu.add_command(label="Выход", command=quit)
    fileclear = Menu(mainmenu, tearoff=0)
    fileclear.add_command(label="Очистить данные")
    helpmenu = Menu(mainmenu, tearoff=0)
    helpmenu.add_command(label="О программе", command=Page().help_me)
    mainmenu.add_cascade(label="Файл", menu=filemenu)
    mainmenu.add_cascade(label="Операции", menu=fileclear)
    mainmenu.add_cascade(label="Справка", menu=helpmenu)

    root.mainloop()
