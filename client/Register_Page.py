
import tkinter as tk
from tkinter import messagebox

import Login_Page
import Main_Window

class Register_Page(tk.Frame):

    def __init__(self,master):
        super().__init__(master)
        self.master.geometry("{}x{}".format(400, 400))
        self.master.title("Rejestracja")
        self.create_widgets()


    def create_widgets(self):
        self.login = tk.Label(self.master,text="Podaj login:")
        self.login_entry = tk.Entry(self.master,bd=5)

        self.password = tk.Label(self.master,text="Podaj haslo:")
        self.password_entry = tk.Entry(self.master,bd=5)

        self.imie = tk.Label(self.master,text="Podaj imie:")
        self.imie_entry = tk.Entry(self.master,bd=5)

        self.nazwisko = tk.Label(self.master,text="Podaj nazwisko:")
        self.nazwisko_entry = tk.Entry(self.master,bd=5)


        self.back = tk.Button(self.master)
        self.back["text"] = u"Powrot"

        self.register = tk.Button(self.master)
        self.register["text"] = u"Zarejestruj"


        self.login.grid(row=0,column=0,ipadx=50,ipady=20)
        self.login_entry.grid(row=0,column=1)

        self.password.grid(row=1,column=0,ipady=20)
        self.password_entry.grid(row=1,column=1)

        self.imie.grid(row=2,column=0,ipady=20)
        self.imie_entry.grid(row=2,column=1)

        self.nazwisko.grid(row=3,column=0,ipady=20)
        self.nazwisko_entry.grid(row=3,column=1)



        self.back.grid(row=5,column=0)
        self.register.grid(row=5,column=1)

        self.back["command"] = self.powrot
        self.register["command"] = self.rejestracja


    def powrot(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Login_Page.Login_Page(root)
        self.child.mainloop()

    def rejestracja(self):
        self.__login = self.login_entry.get()
        self.__password = self.password_entry.get()
        self.__imie = self.imie_entry.get()
        self.__nazwisko = self.nazwisko_entry.get()


        self.master.destroy()
        root  = tk.Tk()
        self.child = Main_Window.Main_Window(master=root)
        self.child.mainloop()



        good_data = True
        #checking data on register
        #czasem nie lapie poczatkowych warunków?

        if(len(self.__login) < 4):
            messagebox.showinfo("Blad!","Zbyt krotki login!")
            good_data = False
        if(len(self.__password) < 4):
            messagebox.showinfo("Blad!","Zbyt krotkie haslo!")
            good_data = False




        """

        if(good_data):
            krotka = (last_index("SELECT * from user")+1,self.__login,self.__password,self.__imie,self.__nazwisko,self.__wzrost)
            print(krotka)
            if(check_if_egzist_data_in_database("SELECT * from user",krotka,[1]) == False):
                u = User(last_index("SELECT * from user")+1,self.__login,self.__password,self.__imie,self.__nazwisko,self.__wzrost)
                if(u.save_to_database()):
                    messagebox.showinfo("Sukces!","Pomyslna rejestracja!")
                else:
                    messagebox.showinfo("Blad!","Blad podczas rejestracji!")
        
        """