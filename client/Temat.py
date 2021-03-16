

class Temat:

    def __init__(self,id,tytul,opis,czyZajety,idPracownik):
        self.__id = int(id)
        self.__tytul = tytul
        self.__opis = opis
        self.__czyZajety = int(czyZajety)
        self.__idPracownik = int(idPracownik)

    def __str__(self):
        return self.__tytul

    def get_opis(self):
        return self.__opis

    def get_id(self):
        return self.__id