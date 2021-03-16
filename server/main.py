import socket
import database_methods

def main():
    client = socket.socket()
    host = socket.gethostname()
    port = 12345

    client.bind((host,port))
    client.listen(5)

    while True:
        c, addr = client.accept()
        print ('kod: ',addr)
        dataFromClient = c.recv(1024)

        if(dataFromClient.decode() != ""):

            dataFromClient = dataFromClient.decode().split("\t")

            if(dataFromClient[0] == "logowanie"):
                odp = database_methods.check_account_in_database(dataFromClient[1],dataFromClient[2])

                # id imie nazwisko
                if(odp[0] == True):
                    print(odp[1][0])
                    odp = str(odp[1][0][0]) + "\t" + str(odp[1][0][1]) + "\t" + str(odp[1][0][2]) + "\t" + str(odp[1][0][3]) + "\t" + str(odp[1][0][4]) + "\t" + str(odp[1][0][5])
                    #print(odp)
                    c.send(odp.encode())
                if(odp[0] == False):
                    odp = "error"
                    c.send(odp.encode())

            if(dataFromClient[0] == "lista_wolnych_tematow"):
                odp = database_methods.check_free_topic()
                if(odp[0] == True):
                    res = ""
                    print(odp)
                    for index in range(len(odp[1])):
                        res += str(odp[1][index][0]) + "\t" + str(odp[1][index][1]) + "\t" + str(odp[1][index][2]) + "\t" + str(odp[1][index][3]) + "\t" + str(odp[1][index][4]) + "\t"
                    c.send(res.encode())


                if(odp[0] == False):
                    odp = "error"
                    c.send(odp.encode())

            if(dataFromClient[0] == "wybrano_temat_zespol"):
                database_methods.update_temat(dataFromClient[1],dataFromClient[2])
                res = "Prawidlowo wybrano temat!"
                c.send(res.encode())

            if(dataFromClient[0] == "znajdz_zespol"):
                data = database_methods.find_zespol_by_id_student(dataFromClient[1])
                c.send(data[1].encode())

            if(dataFromClient[0] == "utworz_zespol"):
                data = database_methods.create_new_zespol(dataFromClient[1])
                c.send(str(data).encode())

            if(dataFromClient[0] == "usun_zespol"):
                data = database_methods.delete_zespol(dataFromClient[1],dataFromClient[2])
                c.send(data.encode())
            if(dataFromClient[0] == "moj_zespol"):
                data = database_methods.pokaz_moj_zespol(dataFromClient[1])
                c.send(data.encode())
            if(dataFromClient[0] == "usun_osobe"):
                data = database_methods.usun_osobe(dataFromClient[1],dataFromClient[2],dataFromClient[3],dataFromClient[4])
                c.send(data.encode())
            if(dataFromClient[0] == "znajdz_wolnych_studentow"):
                data = database_methods.znajdz_studentow_bez_zespolu()
                c.send(data.encode())
            if(dataFromClient[0] == "dodaj_studenta"):
                data = database_methods.dodaj_studenta(dataFromClient[1],dataFromClient[2],dataFromClient[3],dataFromClient[4])
                c.send(data.encode())
            if(dataFromClient[0] == "wyswietl_temat"):
                data = database_methods.wyswielt_temat(dataFromClient[1])
                c.send(data.encode())
            if(dataFromClient[0] == "dodaj_temat"):
                data = database_methods.dodaj_temat(dataFromClient[1],dataFromClient[2],dataFromClient[3])
                c.send(data.encode())
            if(dataFromClient[0] == "usun_temat"):
                data = database_methods.usun_temat(dataFromClient[1],dataFromClient[2])
                c.send(data.encode())

        c.close()





if __name__ == "__main__":
    main()