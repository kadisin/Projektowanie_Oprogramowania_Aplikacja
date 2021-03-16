import socket


class Student:

    def __init__(self,id,imie,nazwisko,login,password,czyPosiadaZespol):
        self.__id = int(id)
        self.__imie = imie
        self.__nazwisko = nazwisko
        self.__login = login
        self.__password = password
        self.__czyPosiadaZespol = int(czyPosiadaZespol)
        self.__idZespol = self.get_number_zespol()
        print(self.__idZespol)

    def get_idZespol(self):
        return self.__idZespol
    def ustaw_zespol(self,id_zespol):
        self.__czyPosiadaZespol = 1
        self.__idZespol = id_zespol
    def usun_zespol(self):
        self.__czyPosiadaZespol = 0
        self.__idZespol = -1

    def get_number_zespol(self):
        client = socket.socket()
        host = socket.gethostname()
        port = 12345

        client.connect((host, port))

        data = "znajdz_zespol\t" + str(self.get_id()) + "\t"
        client.send(data.encode())

        reply = client.recv(1024)
        reply = reply.decode()
        if(reply == "-1"):
            self.__czyPosiadaZespol = 0
        else:
            self.__czyPosiadaZespol = 1
        return reply


    def czyPosiadamZespol(self):
        if (self.__czyPosiadaZespol == 1):
            return True
        else:
            return False


    def __str__(self):
        status = ""
        if(self.__czyPosiadaZespol == 1):
            status = " w zespole"
        else:
            status = " bez zespolu"
        str_ = "Imię i nazwisko:    " + self.__imie + " " + self.__nazwisko + "\n" + "      student      \n"  + "      status:  " + status
        return str_

    def get_id(self):
        return self.__id