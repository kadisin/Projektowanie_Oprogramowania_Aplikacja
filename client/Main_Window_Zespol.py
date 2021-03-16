import socket
import tkinter as tk
from tkinter import messagebox

import Find_New_Users
import Main_Window
import User


class Main_Window_Zespol(tk.Frame):

    def __init__(self,user: User,master=None):
        super().__init__(master)
        self.__user = user
        self.master.title("Zarzadzaj zespolem!")
        self.master.geometry("{}x{}".format(350,400))
        self.create_widgets()



    def create_widgets(self):



        self.var1 =tk.StringVar()

        self.label = tk.Label(self.master,text="Zespol:")
        self.list_student = tk.Listbox(self.master,width=40,height=10,bd=2,highlightcolor="light blue",selectbackground="green",
                                        selectmode=tk.SINGLE)

        self.complete_the_list()
        self.button_cofnij = tk.Button(self.master,text="Cofnij",width=12,height=2,command=self.cofnij)
        self.dodaj_osobe = tk.Button(self.master,text="Dodaj osobe",width=12,height=2,command=self.dodajOsobe)
        self.usun_osobe = tk.Button(self.master,text="Usun osobe",width=12,height=2, command=self.usunOsobe)
        self.pokaz_informacje = tk.Button(self.master,text="Informacje",width=12,height=2,command=self.pokazInformacje)
        self.pokaz_temat = tk.Button(self.master, text="Temat", width=12,height=2,command=self.pokazTemat)

        self.label.grid(row=0,columnspan=3,ipadx=30,ipady=10)
        self.list_student.grid(rowspan=3,columnspan=3)
        self.button_cofnij.grid(row=4,column=0)
        self.dodaj_osobe.grid(row=4,column=1)
        self.usun_osobe.grid(row=4,column=2)
        self.pokaz_informacje.grid(row=5,column=0)
        self.pokaz_temat.grid(row=5,column=1)



    def complete_the_list(self):
        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))

        data = "moj_zespol\t" + str(self.__user.get_idZespol()) + "\t"
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        reply = reply.split("\t")
        for index in range(len(reply)):
            self.list_student.insert('end',reply[index])


    def pokazTemat(self):
        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))

        data = "wyswietl_temat\t" + str(self.__user.get_idZespol())
        print(data)
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        reply = reply.split("\t")
        print(reply)
        if(len(reply) == 1 ):
            messagebox.showerror("Bład!","Zespol nie posiada tematu!")
        else:
            messagebox.showinfo("",reply[1]+"\n"+reply[2])
    def cofnij(self):
        self.master.destroy()
        root = tk.Tk()
        app = Main_Window.Main_Window(self.__user,master=root)
        app.mainloop()
    def dodajOsobe(self):
        self.master.destroy()
        root = tk.Tk()
        app = Find_New_Users.Find_New_Users(self.__user,master=root)
        app.mainloop()
    def pokazInformacje(self):
        value = self.list_student.get(self.list_student.curselection())
        messagebox.showinfo("Informacja",value)

    def usunOsobe(self):
        value = self.list_student.get(self.list_student.curselection())
        print(value.split(" "))

        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))

        data = "usun_osobe\t" + str(self.__user.get_id()) + "\t" + str(self.__user.get_idZespol()) + "\t" + str(value.split(" ")[0]) + "\t" + str(value.split(" ")[1])
        print(data)
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        #reply = reply.split("\t")
        print(reply)
        if(reply == "ok"):
            messagebox.showinfo("Sukces!","Pomyślnie usunięto członka zespołu!")
            self.master.destroy()
            root = tk.Tk()
            self.child = Main_Window_Zespol(self.__user,master=root)
            self.child.mainloop()
        else:
            messagebox.showerror("Blad!","Nie mozna usunac czlonka!\n"
                                         "Upewnij się, ze jestes liderem!")


def main():
    root = tk.Tk()
    app = Main_Window_Zespol(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()