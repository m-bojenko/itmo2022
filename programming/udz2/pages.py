from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
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

        loadimage = PhotoImage(file='btn.png')
        # TODO: разобраться почему не работает

        self.bt_add = Button(buttonframe, text='Добавить ТС', bg='white', command=p1.show_page, width=20, height=5)
        self.bt_add.pack(padx=5, pady=5)
        self.bt_delete = Button(buttonframe, text='Удалить ТС', bg='white', command=p2.show_page, width=20, height=5)
        self.bt_delete.pack(padx=5, pady=5)
        self.bt_search = Button(buttonframe, text='Поиск ТС', bg='white', command=p3.show_page, width=20, height=5)
        self.bt_search.pack(padx=5, pady=5)
        self.bt_app = Button(buttonframe, text='Подать заявку', bg='white', command=p4.show_page, width=20, height=5)
        self.bt_app.pack(padx=5, pady=5)
        self.bt_find = Button(buttonframe, text='Подобрать ТС', bg='white', command=p5.show_page, width=20, height=5)
        self.bt_find.pack(padx=5, pady=5)
        p1.show_page()


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show_page(self):
        self.lift()

    def help_me(self):
        help_root = Tk()
        help_root['bg'] = '#fafafa'  # background
        help_root.title('Справка')  # title of window
        help_root.geometry('900x120')  # size of the window
        help_root.resizable(width=False, height=False)  # user can't change size of the window

        help_root.iconbitmap('help.ico')

        Label(help_root, text='Это программа \"Калькулятор\" с двумя режимами: Классический калькулятор и Прямоугольник.',
              bg='#fafafa').place(x=5, y=5)
        # TODO: Переделать справку на данное приложение


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
            if num[0] not in letters or not num[1].isdigit() or not num[2].isdigit() or not num[3].isdigit() or num[4] not in letters or num[5] not in letters:
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


class Page2(Page):
    """ Удаление Транпортного средства """

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        cars = DataBase().show_transport()
        cars_text = []  # список со строками (1 строка - информация по машине)
        for i in cars:
            cars_text.append(f'{i[0]}.  {i[1]} {i[2]} {i[3]} {i[4]} {i[5]} {i[6]} {i[7]} {i[8]}')

        self.frame0 = Frame(self)
        self.frame0.pack(fill='x')

        self.label_brand = Label(self.frame0, text='Удаление Транспортного средства из базы данных', font=35)
        self.label_brand.pack(fill='x', padx=5, pady=10, expand=True)

        self.var = StringVar()
        self.combobox = ttk.Combobox(self, textvariable=self.var, width=30)
        self.combobox['values'] = cars_text
        self.combobox['state'] = 'readonly'
        self.combobox.pack(side='top', fill='x', pady=10, padx=30)

        self.frame1 = Frame(self)
        self.frame1.pack(fill='x', padx=30)

        self.add_btn = Button(self.frame1, text='Добавить', width=15, command=self.action)
        self.add_btn.pack(side='right', padx=20, pady=10)
        self.clear_btn = Button(self.frame1, text='Очистить', width=15, command=self.clear)
        self.clear_btn.pack(side='right', padx=20, pady=10)

    def action(self):
        pass

    def clear(self):
        pass


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

        var = StringVar()
        combobox = ttk.Combobox(self, textvariable=var, width=30)
        combobox['values'] = cars_text
        combobox['state'] = 'readonly'
        combobox.pack(side='top', fill='x', pady=10, padx=30)


class Page4(Page):
    """ Подача заявки """

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Label(self, text='Page4').pack(side="top", fill="both", expand=True)


class Page5(Page):
    """ Подбор траспортного средства """

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        Label(self, text='Page5').pack(side="top", fill="both", expand=True)


if __name__ == "__main__":
    root = Tk()
    main = Window(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x500")
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
