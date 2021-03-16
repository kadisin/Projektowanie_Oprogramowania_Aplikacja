import tkinter as tk
from tkinter import messagebox


class Change_Password(tk.Frame):

    def __init__(self,master=None):
        super().__init__(master)
        self.master.title("Zmien Haslo")
        self.master.geometry("{}x{}".format(400,300))
        self.create_widgets()

    def create_widgets(self):

        self.old_password = tk.Label(self.master,text="Podaj poprzednie haslo:")
        self.old_password_entry = tk.Entry(self.master,bd=5)

        self.new_password = tk.Label(self.master,text="Podaj nowe haslo:")
        self.new_password_entry = tk.Entry(self.master,bd=5)



        self.button_potwierdz = tk.Button(self.master,width=10,height=3,text="Potwierdz",command=self.potwierdz)
        self.button_cofnij = tk.Button(self.master,width=10,height=3,text="Cofnij",command=self.cofnij)


        self.old_password.grid(row=0,column=0,padx=20,pady=20)
        self.old_password_entry.grid(row=0,column=1)
        self.new_password.grid(row=1,column=0,padx=20,pady=10)
        self.new_password_entry.grid(row=1,column=1)


        self.button_cofnij.grid(row=3,column=0)
        self.button_potwierdz.grid(row=3,column=1)


    def potwierdz(self):

        self.__old_password = self.old_password_entry.get()
        self.__new_password = self.new_password_entry.get()

        messagebox.showinfo("Sukces","Pomyslnie zmieniono haslo!")
        self.master.destroy()


    def cofnij(self):
        self.master.destroy()
