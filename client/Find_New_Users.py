import socket
import tkinter as tk
from tkinter import messagebox
import User
import Main_Window
import Main_Window_Zespol
class Find_New_Users(tk.Frame):


    def __init__(self,user: User,master=None):
        super().__init__(master)
        self.__user = user
        self.master.title("Znajdz nowych czlonkow!")
        self.master.geometry("{}x{}".format(400,550))
        self.create_widgets()


    def create_widgets(self):
        #self.opis_tabeli = tk.Label(self.master, text="Wybierz Osobe", height=5)
        self.lista_studenci = tk.Listbox(self.master, width=40, height= 20,bd=2,highlightcolor="light blue",selectbackground="green",
                                        selectmode=tk.SINGLE)

        self.button_dodaj = tk.Button(self.master,text="Dodaj",width=15,height=3,command=self.dodajCzlonka)
        self.button_powrot = tk.Button(self.master,text="Powrot",width=15,height=3,command=self.powrot)


        self.var1 = tk.StringVar()


        self.find_all_free_students()


        #self.opis_tabeli.grid(row=0,columnspan=2)
        self.lista_studenci.grid(row=1,columnspan=2,padx=30,pady=20)
        self.button_powrot.grid(row=2,column=0)
        self.button_dodaj.grid(row=2,column=1)




    def find_all_free_students(self):
        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))

        data = "znajdz_wolnych_studentow\t"
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        reply = reply.split("\t")
        #print(reply)
        for student in reply:
            self.lista_studenci.insert('end',student)





    def dodajCzlonka(self):
        value = self.lista_studenci.get(self.lista_studenci.curselection())
        print(value)
        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))

        data = "dodaj_studenta\t" + str(self.__user.get_id()) + "\t" + str(self.__user.get_idZespol()) + "\t" + str(value.split(" ")[0]) + "\t" + str(value.split(" ")[1])
        print(data)
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        reply = str(reply)
        print(reply)
        #reply = reply.split("\t")
        if(reply == 'pelna'):
            messagebox.showerror("Bład!","Zespol jest pelny!")
        if(reply == 'notlider'):
            messagebox.showerror("Blad!","Tylko lider moze dodawać członkow!")
        if(reply == 'ok'):
            messagebox.showinfo("Sukces!","Pomyslnie dodano czlonka do grupy!")
            self.master.destroy()
            root = tk.Tk()
            self.child = Main_Window_Zespol.Main_Window_Zespol(self.__user,master=root)
            self.child.mainloop()





    def powrot(self):
        self.master.destroy()
        root = tk.Tk()
        app = Main_Window.Main_Window(self.__user,master=root)
        app.mainloop()
def main():
    root = tk.Tk()
    app = Find_New_Users(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()