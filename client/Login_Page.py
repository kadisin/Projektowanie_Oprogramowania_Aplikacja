import tkinter as tk
from tkinter import messagebox
import socket
import Register_Page
import Main_Window
import User

class Login_Page(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master.geometry("{}x{}".format(400, 200))
        self.master.title("Autoryzacja")
        self.create_widgets()

    def create_widgets(self):
        self.login_1 = tk.Label(self.master, text="Login:")
        self.login_enter = tk.Entry(self.master, bd=5)

        self.password_1 = tk.Label(self.master, text="Password:")
        self.password_enter = tk.Entry(self.master, bd=5)

        self.register = tk.Button(self.master)
        self.register["text"] = u"Rejestracja"

        self.zaloguj = tk.Button(self.master)
        self.zaloguj["text"] = u"Zaloguj sie"

        self.login_1.grid(row=0, column=0, ipadx=50, ipady=20)
        self.login_enter.grid(row=0, column=1)

        self.password_1.grid(row=1, column=0)
        self.password_enter.grid(row=1, column=1)

        self.register.grid(row=2, column=0,padx=30,pady=10)
        self.zaloguj.grid(row=2, column=1,padx=10,pady=10)

        self.register["command"] = self.rejestracja
        self.zaloguj["command"] = self.logowanie

    def rejestracja(self):
        self.master.destroy()
        root = tk.Tk()
        self.child = Register_Page.Register_Page(root)
        self.child.mainloop()

    def logowanie(self):

        self.user_login = self.login_enter.get()
        self.user_password = self.password_enter.get()

        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host,port))

        data = "logowanie\t" + self.user_login + "\t" + self.user_password
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        if ( reply == 'error'):
            messagebox.showerror("","Nieprawidłowe dane!")
        else:
            reply = reply.split('\t')
            #print(reply)
            user = User.Student(reply[0], reply[1], reply[2], reply[3], reply[4], reply[5])
            messagebox.showinfo("","Pomyślne logowanie!")
            self.master.destroy()
            root = tk.Tk()
            app = Main_Window.Main_Window(user,master=root)
            app.mainloop()


        client.close()