import tkinter as tk
from tkinter import messagebox

import Login_Page


class StartWindow(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master.geometry("{}x{}".format(400,400))
        self.master.title("ZPI_PROJEKT")
        self.pack()
        self.create_widgets()


    def create_widgets(self):
        self.start = tk.Button(self)
        self.start["text"] = u"START"
        self.start["command"] = self.start_
        self.start.pack(side="top")

        self.pomoc = tk.Button(self)
        self.pomoc["text"] = u"O Programie"
        self.pomoc["command"] = self.pomoc_
        self.pomoc.pack(side="bottom")

    def start_(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Login_Page.Login_Page(root)
        self.child.mainloop()
    def pomoc_(self):
        pass

def main():
    root = tk.Tk()
    app = StartWindow(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()