# from tkinter import *
# from tkinter.messagebox import showinfo, showerror
#
# root = Tk()  # our window
#
#
# def btn_click():
#
#     login = loginInput.get()
#     password = passField.get()
#
#     info_str = f'Данные: {str(login)}, {str(password)}'
#
#     if len(login) > 10:
#         showerror(title='', message='Error always!!!!')
#     else:
#         showinfo(title='Название', message=info_str)
#
#
# root['bg'] = '#fafafa'  # background
# root.title('Name of program')  # title of window
# # root.wm_attributes('-alpha', 0.7)  # prozrachnost'
# root.geometry('400x350')  # size of the window
#
# root.resizable(width=False, height=False)  # user can't change size of the window
#
# canvas = Canvas(root, width=400, height=350)
# canvas.pack()
#
# frame = Frame(root, bg='red')
# frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
#
# title = Label(frame, text='Some text', bg='gray', font=40)
# title.pack()
# btn = Button(frame, text='Button', bg='yellow', command=btn_click)
# btn.pack()
#
# loginInput = Entry(frame, bg='white')
# loginInput.pack()
#
# passField = Entry(frame, bg='white', show='*')
# passField.pack()
#
# root.mainloop()  # for window to work
#

import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)


class Page2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 2")
        label.pack(side="top", fill="both", expand=True)


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 3")
        label.pack(side="top", fill="both", expand=True)


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x400")
    root.mainloop()
