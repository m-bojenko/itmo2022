from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from exceptions import *


class Window:
    def work(self):

        root = Tk()  # our window

        root['bg'] = '#fafafa'  # background
        root.title('ЛогиСтатик')  # title of window
        # root.wm_attributes('-alpha', 0.7)  # prozrachnost'
        root.geometry('800x500')  # size of the window
        root.iconbitmap('truck.ico')

        root.resizable(width=False, height=False)  # user can't change size of the window

        frame = Frame(root, bg='#E6E6FA')
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.pos = StringVar(value='begin')

        self.bt_add = Button(frame, text='Добавить ТС', command=lambda : self.bttn_add(), bg='white')
        self.bt_add.place(x=0, y=0, width=150, height=50)
        self.bt_delete = Button(frame, text='Удалить ТС', command=lambda : self.bttn_delete(), bg='white')
        self.bt_delete.place(x=0, y=50, width=150, height=50)
        self.bt_search = Button(frame, text='Поиск ТС', bg='white')
        self.bt_search.place(x=0, y=100, width=150, height=50)
        self.bt_app = Button(frame, text='Подать заявку', bg='white')
        self.bt_app.place(x=0, y=150, width=150, height=50)
        self.bt_find = Button(frame, text='Подобрать ТС', bg='white')
        self.bt_find.place(x=0, y=200, width=150, height=50)

        #  Меню
        mainmenu = Menu(root)
        root.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Выход", command=root.quit)

        fileclear = Menu(mainmenu, tearoff=0)
        fileclear.add_command(label="Очистить данные")

        helpmenu = Menu(mainmenu, tearoff=0)
        helpmenu.add_command(label="О программе", command=self.help_me)

        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Операции", menu=fileclear)
        mainmenu.add_cascade(label="Справка", menu=helpmenu)

        root.mainloop()  # for window to work

    def bttn_add(self):
        self.pos = StringVar(value='add')
        self.right_window()

    def bttn_delete(self):
        self.pos = StringVar(value='delete')
        self.right_window()

    def right_window(self):
        if self.pos.get() == 'add':
            self.bt_add.config(bg='#E6E6FA')
        else:
            self.bt_add.config(bg='white')
        if self.pos.get() == 'delete':
            self.bt_delete.config(bg='#E6E6FA')
        else:
            self.bt_delete.config(bg='white')

    def help_me(self):
        help_root = Tk()
        help_root['bg'] = '#fafafa'  # background
        help_root.title('Справка')  # title of window
        help_root.geometry('900x120')  # size of the window
        help_root.resizable(width=False, height=False)  # user can't change size of the window

        help_root.iconbitmap('help.ico')

        Label(help_root, text='Это программа \"Калькулятор\" с двумя режимами: Классический калькулятор и Прямоугольник.',
              bg='#fafafa').place(x=5, y=5)


Window().work()
