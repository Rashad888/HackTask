from tkinter import Tk, RIGHT, BOTH, RAISED, LEFT, BOTTOM, Label, X, Y, TOP, filedialog, Toplevel, Text, Scrollbar, \
    Listbox, END
from tkinter.ttk import Button, Frame, Style, Entry
import tkinter.messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack(fill=BOTH, expand=True,)
        self.get_some_style()
        self.create_widgets()
        self.master.title("Отслеживание полетов")
        self.master.resizable(True, True)



    def create_widgets(self):

        main_style = Style()
        main_style.configure("P.TFrame", background="navajo white")

        frame1 = Frame(self)
        frame1.pack(fill=BOTH, pady=100)

        lbl1 = Label(frame1, text="Добавьте файл с данными о трекинге", width=30)
        lbl1.pack(side=LEFT, padx=5, pady=0)

        global entry1
        entry1 = Entry(frame1)
        entry1.pack(side=LEFT, fill=X, padx=5, expand=True)

        self.btnAdd = Button(frame1, text="Добавить")
        self.btnAdd.pack(side=LEFT, fill=X, padx=5, expand=True)
        self.btnAdd.bind("<ButtonRelease>", self.open_file)

        frame2 = Frame(self)
        frame2.pack(fill=X, pady=50)

        lbl1 = Label(frame2, text="Укажите путь сохранения результата", width=30)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        global entry2
        entry2 = Entry(frame2)
        entry2.pack(side=LEFT, fill=X, padx=5, expand=True)

        self.btnAdd = Button(frame2, text="Выбрать")
        self.btnAdd.pack(side=LEFT, fill=X, padx=5, expand=True)
        self.btnAdd.bind("<ButtonRelease>", self.save_file)

        self.btnExit = Button(self, text="Выход")
        self.btnExit["command"] = root.destroy
        self.btnExit.pack(side=BOTTOM,pady=10)

        self.btnHello = Button(self, text="Анализ", command=create_window)
        self.btnHello.pack(side=BOTTOM, padx=5, pady=5)


    def open_file(self, env):
        entry1.delete(0, 'end')
        env.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                  filetypes=(("text files", "*.txt"), ("all files", "*")))
        entry1.insert(0, env.filename)

    def save_file(self, env):
        entry2.delete(0, 'end')
        directory = filedialog.askdirectory()
        entry2.insert(0,directory)

    def get_some_style(self):
        s = Style()
        s.configure("My.TFrame", background='white')

        frame_main = Frame(self, style="My.TFrame", height=100)
        frame_main.pack(fill=BOTH, ipady=5, ipadx=10)

        self.btnAbout = Button(frame_main, text="Помощь")
        self.btnAbout.pack(side=RIGHT, padx=10, expand=True)

        self.btnAbout = Button(frame_main, text="Авторы")
        self.btnAbout.pack(side=RIGHT, padx=10, expand=True)

        self.btnAbout = Button(frame_main, text="О программе")
        self.btnAbout.pack(side=RIGHT, padx=10, expand=True)

        self.img = tkinter.PhotoImage(file = 'C:\Portfolio\Hackaton\HackTask\Desktop\source\picture1.png')
        self.pic = Label(frame_main, image=self.img)
        self.pic.pack(side=LEFT, expand=True)


def create_window():
    window = Toplevel(root)
    window.title("Выборка полетов")
    window.geometry("1200x900")

    frame_ch = Frame(window)
    frame_ch.pack(fill=BOTH)

    scrollbar = Scrollbar(frame_ch)
    scrollbar.pack(side=RIGHT, fill=Y)

    text = open(str(entry1.get()), encoding='utf-8').readlines()
    text = ''.join(text)
    textline = Text(frame_ch, yscrollcommand=scrollbar.set, height=50)
    textline.insert(1.0, text)
    textline.pack(side=RIGHT, fill=Y, expand=True)
    scrollbar.config(command=textline.yview)

    save = open(str(entry2.get())+"\\result.txt", 'w')
    save.write("Ответ")
    save.close()


if __name__ == '__main__':
    root = Tk()
    root.geometry("1200x700")
    app = Application(master=root)
    root.mainloop()
