import tkinter as tk
from tkinter import messagebox
import User
import Main_Window
import Choise_Temat

class Choise_Opiekun(tk.Frame):

    def __init__(self,user: User,master=None):
        super().__init__(master)
        self.master.title("Wybierz Opiekuna")
        self.__user = user
        self.master.geometry("{}x{}".format(400,400))
        self.create_widgets()


    def create_widgets(self):

        self.var1 = tk.StringVar()

        self.lista_opiekunow = tk.Listbox(self.master, width=45, height=15, bd=2, highlightcolor="light blue",
                                            selectbackground="green",
                                            selectmode=tk.SINGLE)


        self.button_wybierz = tk.Button(self.master,text="Wybierz",command=self.wybierzTemat)
        self.button_cofnij = tk.Button(self.master,text="Powrot",command=self.cofnij)
        self.button_informacje = tk.Button(self.master, text="Pokaz Informacje", command=self.informacjeOpiekun)

        self.lista_opiekunow.grid(row=0,columnspan=3,padx=15)
        self.button_cofnij.grid(row=2,column=0)
        self.button_informacje.grid(row=2,column=1)
        self.button_wybierz.grid(row=2,column=2)

        self.list_items = ["Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski",
                           "Prof. dr. hab. inż. Włodzimierz Bielecki\n\n", "Dr Anna Kaczmarek", "Dr Andrzej Kowalski"
                           ]

        for item in self.list_items:
            self.lista_opiekunow.insert('end',item)


    def wybierzTemat(self):
        #do sth
        messagebox.showinfo("Sukces!", "Prawidlowo wybrano opiekuna!")
        self.master.destroy()
        root = tk.Tk()
        app = Choise_Temat.Choise_Temat(self.__user,master=root)
        app.mainloop()


    def cofnij(self):
        self.master.destroy()
        root = tk.Tk()
        app = Main_Window.Main_Window(self.__user,master=root)
        app.mainloop()

    def informacjeOpiekun(self):
        messagebox.showinfo("Informacja","Informacje na temat opiekuna!")