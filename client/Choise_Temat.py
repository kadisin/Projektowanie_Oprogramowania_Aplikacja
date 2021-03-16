import tkinter as tk
from tkinter import messagebox
import socket
import Main_Window
import Temat
import User
class Choise_Temat(tk.Frame):

    def __init__(self,user: User,master=None):
        super().__init__(master)
        self.master.title("Wybierz Temat")
        self.__user = user
        self.master.geometry("{}x{}".format(400,400))
        self.create_widgets()


    def create_widgets(self):

        self.var1 = tk.StringVar()

        self.lista_tematow = tk.Listbox(self.master, width=45, height=15, bd=2, highlightcolor="light blue",
                                            selectbackground="green",
                                            selectmode=tk.SINGLE)


        self.button_wybierz = tk.Button(self.master,text="Wybierz",command=self.wybierzTemat)
        self.label_opiekun = tk.Label(self.master,text="Opiekun:    Dr Anna Kaczmarek")
        self.button_cofnij = tk.Button(self.master,text="Powrot",command=self.cofnij)
        self.button_informacje = tk.Button(self.master, text="Pokaz Informacje", command=self.informacjeTemat)

        self.lista_tematow.grid(row=0,columnspan=3,padx=15, ipady=5)
        #self.label_opiekun.grid(row=1,columnspan=3)
        self.button_cofnij.grid(row=2,column=0)
        self.button_wybierz.grid(row=2,column=2)
        self.button_informacje.grid(row=2,column=1)

        self.list = []
        self.add_topics_to_list()




    def wybierzTemat(self):

        clicked_index = 0
        nazwa = self.lista_tematow.get(self.lista_tematow.curselection())
        for index in range(len(self.list)):
            if (self.list[index].__str__() == nazwa):
                clicked_index = index
        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))
        #print(self.list[clicked_index].get_id())
        data = "dodaj_temat\t" + str(self.__user.get_id()) + "\t" + str(self.__user.get_idZespol()) + "\t"+ str(self.list[clicked_index].get_id())
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        print(reply)
        # odpowiedz!
        if(reply == "posiadamtemat"):
            messagebox.showerror("Blad!","Twoj zespol posiada juz temat!")
        elif (reply == "nielider"):
            messagebox.showerror("Blad!","Tylko lider moze wybrać temat!")
        elif(reply == "ok"):
            messagebox.showinfo("","Pomyslnie wybrano temat!")
            self.master.destroy()
            root = tk.Tk()
            self.child = Main_Window.Main_Window(self.__user,master=root)
            self.child.mainloop()



    def add_topics_to_list(self):
        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))

        data = "lista_wolnych_tematow\t"
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        print(reply)
        if (reply == 'error'):
            self.list = []
        else:
            reply = reply.split('\t')
            pom_list = []
            for index in range(len(reply)):
                if(index % 5 == 0 and index != 0):
                    print(pom_list)
                    t = Temat.Temat(pom_list[0],pom_list[1],pom_list[2],pom_list[3],pom_list[4])
                    self.list.append(t)
                    pom_list = [reply[index]]
                else:
                    pom_list.append(reply[index])
            for index in range(len(self.list)):
                self.lista_tematow.insert('end',self.list[index].__str__())


        client.close()


    def cofnij(self):
        self.master.destroy()
        root = tk.Tk()
        app = Main_Window.Main_Window(self.__user,master=root)
        app.mainloop()

    def informacjeTemat(self):
        clicked_index = 0
        nazwa = self.lista_tematow.get(self.lista_tematow.curselection())
        for index in range(len(self.list)):
            if(self.list[index].__str__() == nazwa):
                clicked_index = index

        messagebox.showinfo("Informacja",self.list[clicked_index].get_opis())