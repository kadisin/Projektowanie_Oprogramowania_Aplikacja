import socket
import tkinter as tk
from tkinter import messagebox

import Find_New_Users
import Main_Window_Zespol
import Change_Password
import Choise_Temat
import Choise_Opiekun
import User

class Main_Window(tk.Frame):


    def __init__(self, user: User, master=None):
        super().__init__(master)
        self.__user = user
        self.master.geometry("{}x{}".format(500, 243))
        self.master.title("Strona Glowna")

        self.create_widgets()

    def create_widgets(self):

        self.menu_ = tk.Menu()

        self.fileMenu = tk.Menu(self.master)
        self.menu_.add_cascade(label='Program', menu=self.fileMenu)

        self.fileMenu.add_command(label='Pomoc', command=self.pomoc)
        self.fileMenu.add_command(label='Autor', command=self.autor)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label='Zakoncz', command=self.onExit)

        self.saveMenu = tk.Menu(self.menu_)
        self.menu_.add_cascade(label='Historia', menu=self.saveMenu)

        self.saveMenu.add_command(label='Zmien Haslo', command=self.zmienHaslo)

        self.thirdMenu = tk.Menu(self.menu_)
        self.menu_.add_cascade(label="Zespol", menu=self.thirdMenu)


        self.thirdMenu.add_command(label="Utworz zespol", command=self.utworzZespol)
        self.thirdMenu.add_command(label="Usun zespol", command=self.usunZespol)
        self.thirdMenu.add_separator()
        self.thirdMenu.add_command(label="Zarzadzaj zespolem", command=self.zarzadzajZespolem)
        self.thirdMenu.add_separator()
        self.thirdMenu.add_command(label="Dodaj Czlonkow", command=self.szukajCzlonkow)

        self.forthMenu = tk.Menu(self.menu_)
        self.menu_.add_cascade(label="Temat", menu=self.forthMenu)

        self.forthMenu.add_command(label="Wybierz Temat", command=self.wybierzTemat)
        self.forthMenu.add_command(label="Usun  Temat", command=self.usunTemat)
        self.forthMenu.add_command(label="Wybierz Opiekuna", command=self.wybierzOpiekuna)


        self.master.config(menu=self.menu_)





        self.button_zespol = tk.Button(self.master,width=20,height=5)
        self.button_formularze = tk.Button(self.master,width=20,height=5)
        self.button_kontakt = tk.Button(self.master,width=20,height=5)

        self.button_zespol["text"] = u"Zespol"
        self.button_formularze["text"] = u"Formularz"
        self.button_kontakt["text"] = u"Kontakt"

        self.button_zespol["command"] = self.zarzadzajZespolem



        self.lista_opiekunowie = tk.Listbox(self.master, width=50, height=20,bd=2,highlightcolor="light blue",selectbackground="green",
                                        selectmode=tk.SINGLE)




        self.lista_tematy = tk.Listbox(self.master, width=50, height= 20)



        self.label_user = tk.Label(self.master, text=self.__user.__str__(),width = 35, height=5)


        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()

        self.opis_opiekunowie = tk.Label(self.master,text=" OPIEKUNOWIE ",height=5)
        self.opis_tematy = tk.Label(self.master,text="  SWOBODNE TEMATY  ",height=5)





        self.wybor_opiekunowie = tk.Button(self.master,text="WYBOR")
        #self.wybor_opiekunowie['state'] = "normal"
        self.wybor_tematy = tk.Button(self.master,text="WYBOR")
        self.wybor_opiekunowie['command'] = self.print_selection
        self.wybor_tematy['command'] = self.print_selection_2



        self.footer = tk.Label(self.master)



        #grids
        self.label_user.grid(row=0,columnspan=3,ipadx=10,ipady=10)
        self.button_zespol.grid(row=1,column=0)
        self.button_formularze.grid(row=1,column=1)
        self.button_kontakt.grid(row=1,column=2)






    def print_selection(self):
        value = self.lista_opiekunowie.get(self.lista_opiekunowie.curselection())
        print(value)
        #self.var1.set(value)

    def print_selection_2(self):
        value = self.lista_tematy.get(self.lista_tematy.curselection())
        print(value)


    def autor(self):
        messagebox.showinfo("Autor", "Autorzy\n"
                                     "Dzmitry Lisouski i Tomasz Logisz"
                                     "29.01.2021")
    def pomoc(self):
        messagebox.showinfo("Pomoc!", "Program ZPI")
    def onExit(self):
        self.master.destroy()

    def usunTemat(self):
        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))

        data = "usun_temat\t" + str(self.__user.get_id()) + "\t" + str(self.__user.get_idZespol())
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        if(reply == "nieposiadatemat"):
            messagebox.showerror("Bład!","Twoj zespol nie posiada tematu!")
        elif(reply == "nielider"):
            messagebox.showerror("Bład!","Tylko lider moze usunac temat!")
        elif(reply == "ok"):
            messagebox.showinfo("Sukces!","Prawidlowo usunieto temat!")

    def zmienHaslo(self):
        root = tk.Tk()
        app = Change_Password.Change_Password(master=root)
        app.mainloop()

    def szukajCzlonkow(self):
        self.master.destroy()
        root = tk.Tk()
        app = Find_New_Users.Find_New_Users(self.__user,master=root)
        app.mainloop()

    def utworzZespol(self):
        if(self.__user.czyPosiadamZespol() == True):
            messagebox.showerror("","Jestes juz w zespole!")
        else:
            # utworzenie nowego zespolu
            client = socket.socket()
            host = socket.gethostname()
            port = 12345

            client.connect((host, port))

            data = "utworz_zespol\t" + str(self.__user.get_id()) + "\t"
            client.send(data.encode())

            reply = client.recv(1024)
            reply = reply.decode()
            messagebox.showinfo("Sukces!","Pomyślnie utworzono zespół!")
            self.__user.ustaw_zespol(reply)
            self.master.destroy()
            root = tk.Tk()
            self.child = Main_Window(self.__user,master=root)
            self.child.mainloop()



    def usunZespol(self):
        if (self.__user.czyPosiadamZespol() == False):
            messagebox.showerror("", "Nie posiadasz zespołu!")
        else:
            client = socket.socket()
            host = socket.gethostname()
            port = 12345

            client.connect((host, port))

            data = "usun_zespol\t" + str(self.__user.get_id()) + "\t" + str(self.__user.get_idZespol())
            client.send(data.encode())

            reply = client.recv(1024)
            reply = reply.decode()
            print(reply)
            if(reply == "ok"):
                messagebox.showinfo("Sukces!", "Pomyślnie usunięto zespół!")
                self.__user.usun_zespol()
                self.master.destroy()
                root = tk.Tk()
                self.child = Main_Window(self.__user, master=root)
                self.child.mainloop()
            elif(reply == "nielider"):
                messagebox.showerror("Blad!","Tylko lider moze usunac zespol!")
            elif(reply == "niepustyzespol"):
                messagebox.showerror("Blad!","W zespole musi byc tylko lider!")

    def zarzadzajZespolem(self):
        if (self.__user.czyPosiadamZespol() == False):
            messagebox.showerror("", "Nie posiadasz zespołu!")
        else:
            self.master.destroy()
            root = tk.Tk()
            app = Main_Window_Zespol.Main_Window_Zespol(self.__user,master=root)
            app.mainloop()


    def wybierzTemat(self):

            self.master.destroy()
            root = tk.Tk()
            app = Choise_Temat.Choise_Temat(self.__user,master=root)
            app.mainloop()


    def wybierzOpiekuna(self):
        self.master.destroy()
        root = tk.Tk()
        app = Choise_Opiekun.Choise_Opiekun(self.__user,master=root)
        app.mainloop()


def main():
    root = tk.Tk()
    app = Main_Window(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()




