import pymysql




def check_account_in_database(login,password):
    """
    :param login: user login
    :param password:  user password
    :return: krotka (boolean,user)

    Opis: Metoda służy do sprawdzenia czy istnieje w bazie danych użytkownik o podanym loginie i haśle.
    W przypadku braku użytkownika o podanym loginie i haśle zwrócone zostaje (False,"")
    W przypadku gdy dany użytkownik istnieje w bazie zostaje zwrócone (False,(id_user,imie,nazwisko,login,haslo,maTemat))

    """


    connection = pymysql.connect(host="localhost",user="root",passwd="",database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "SELECT * FROM `student` WHERE `login` = '" + str(login) + "' AND `password` = '" + str(password) + "'"
    #print(retrive)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows) == 0) :
       #nieuzyskana autoryzacja
        return (False,"")

    connection.commit()
    connection.close()
    return (True,rows)

def check_free_topic():
    """
    :return: krotka (Boolean,krotka)

    Opis: Metoda służąca do zwrócenia wszystkich niezajętych tematów.
    W przypadku braku wolnych tematów zostaje zwrócone (False,"")
    W przeciwnym przypadku zostaje zwrócone (True,krotka), gdzie krotka to krotka składająca się z wolnych tematów

    """
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "SELECT * FROM `temat` WHERE `czyZajety` = 0"
    # print(retrive)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if (len(rows) == 0):
        return (False, "")

    connection.commit()
    connection.close()
    return (True, rows)

def update_temat(id_user,id_temat):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "UPDATE `student` SET `maTemat` = '1' WHERE `student`.`Id` = " + str(id_user) + ";"

    # print(retrive)
    cursor.execute(retrive)
    retrive = "UPDATE `temat` SET `czyZajety` = '1' WHERE `temat`.`Id` = " + str(id_temat) + ";"
    cursor.execute(retrive)

    connection.commit()
    connection.close()


def find_zespol_by_id_student(id_student):
    """
    :param id_student: id studenta wysyłającego zapytanie do bazy
    :return: krotka (boolean,int)

    Opis: Metoda służąca do znalezienia id zespołu do którego student o danym id należy
    W przypadku gdy student nie jest przypisany do żadnego zespołu zostaje zwrócone (False,-1)
    W przypadku gdy student jest przypisany do zespołu zwrócone zostaje (True,id_zespolu) gdzie id_zespolu to
    id zespołu do którego student należy.

    """

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()


    retrive = "SELECT * FROM `zespolstudent` WHERE `IdSt` =" + str(id_student)

    cursor.execute(retrive)
    rows = cursor.fetchall()


    connection.commit()
    connection.close()

    if (len(rows) == 0):
        return (False, str(-1))
    else:
        return (True,str(rows[0][1]))

def zespol(id):
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "SELECT * FROM `zespol` WHERE Id =" + str(id)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    list = []

    for index in range(1,5):
        st = "SELECT * FROM `student` WHERE Id =" + str(rows[0][index])
        cursor.execute(st)
        ret = cursor.fetchall()
        list.append(ret[0][1])
        list.append(ret[0][2])

    connection.commit()
    connection.close()
    return list

def create_new_zespol(id_student):

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "INSERT INTO `zespol` VALUES (NULL,NULL," + str(id_student) + ");"
    cursor.execute(retrive)
    print(retrive)

    retrive = "SELECT * FROM `zespol` WHERE IdStudent = " + str(id_student)
    cursor.execute(retrive)

    rows = cursor.fetchall()
    index_zespol = rows[0][0]
    retrive = "INSERT INTO `zespolstudent` VALUES (NULL," + str(index_zespol) + "," + str(id_student)  +");"
    cursor.execute(retrive)

    connection.commit()
    connection.close()

    return index_zespol

def delete_zespol(id_student,id_zespol):

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "SELECT * FROM `zespol` WHERE Id =" + str(id_zespol)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(str(rows[0][2]) == str(id_student)):
        #lider
        retrive = "SELECT * FROM `zespolstudent` WHERE IdZespol=" + str(id_zespol)
        cursor.execute(retrive)
        rows = cursor.fetchall()
        print(rows)
        if(len(rows) == 1):
            retrive = "DELETE FROM `zespolstudent` WHERE `IdZespol` = " + str(id_zespol)
            cursor.execute(retrive)
            retrive = "DELETE FROM `zespol` WHERE `IdStudent` = " + str(id_student)
            cursor.execute(retrive)
            connection.commit()
            connection.close()
            return "ok"
        else:
            return "niepustyzespol"
    else:
        return "nielider"





def pokaz_moj_zespol(id_zespol):
    """
    :param id_zespol: int
    :return: string

    Opis: Metoda służy do zwrócenia imion i nazwisk wszystkich członków zespołu o danym id (id_zespol)
    Wyjściowy napis wygląda w formacie "imie_1 nazwisko1\timie2 nazwisko2\t..." w zależności od ilości członków w zespole.
    """
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "SELECT * FROM `zespolstudent` WHERE `IdZespol` = " + str(id_zespol)
    cursor.execute(retrive)
    #rows = ((9,10,1),(10,10,1))
    rows = cursor.fetchall()
    str_ = ""

    for index in range(len(rows)):
        retrive = "SELECT * FROM `student` WHERE Id = " + str(rows[index][2])
        cursor.execute(retrive)
        os = cursor.fetchall()
        str_ += os[0][1] + " " + os[0][2] + "\t"

    #print(str_)
    connection.commit()
    connection.close()
    return str_


def usun_osobe(id_student,id_zespol,imie_st_do_usuniecia,nazwisko_st_do_usuniecia):
    """
    :param id_student: int
    :param id_zespol: int
    :param imie_st_do_usuniecia: string
    :param nazwisko_st_do_usuniecia: string
    :return: string

    Opis: Metoda służąca do usunięcia studenta z zespołu, osoba usuwająca charakteryzuje się swoim id (id_student)
    Musi ona być liderem zespołu o id - id_zespol.
    Osoba do usunięcia charakteryzuje się imieniem - imie_st_do_usuniecia i nazwiskiem - nazwisko_st_do_usuniecia

    W przypadku gdy osoba wysyłająca zapytanie nie jest liderem zespołu zwrócone zostanie "error\t"
    W przypadku gdy osoba wysyłająca jest liderem i chce usunąć samą siebie zostaje zwrócone "error\tlider\t"
    W przypadku poprawnego usunięcia użytkownika zostaje zwrócone "ok"

    """
    id_student = str(id_student)
    id_zespol = str(id_zespol)
    imie_st_do_usuniecia = str(imie_st_do_usuniecia)
    nazwisko_st_do_usuniecia = str(nazwisko_st_do_usuniecia)

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    search_lider_sql = "SELECT * FROM zespol WHERE Id = " + id_zespol + " AND IdStudent = " + id_student
    cursor.execute(search_lider_sql)
    row_count = cursor.rowcount

    if row_count > 0:
            search_czlonek_sql = "SELECT * FROM student WHERE imie = '" + imie_st_do_usuniecia + "' AND nazwisko = '" + nazwisko_st_do_usuniecia + "'"
            cursor.execute(search_czlonek_sql)
            records = cursor.fetchall()
            id_czlonka = str(-1)
            for row in records:
                id_czlonka = str(row[0])
            if id_czlonka == id_student:
                return "error\tlider\t"
            else:
                sql = "DELETE FROM zespolstudent WHERE IdSt = " + id_czlonka
                cursor.execute(sql)
                connection.commit()
                connection.close()
                return "ok"
    return "error\t"


def znajdz_studentow_bez_zespolu():
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "SELECT `student`.`imie`,`student`.`nazwisko` FROM `student` LEFT JOIN `zespolstudent` ON `zespolstudent`.`IdSt` = `student`.`Id` WHERE `zespolstudent`.`IdSt` IS NULL"
    # rows = ((9,10,1),(10,10,1))
    cursor.execute(retrive)
    rows = cursor.fetchall()
    str_ = ""

    for index in range(len(rows)):
        str_ += rows[index][0] + " " + rows[index][1] + "\t"
    print(str_)
    connection.commit()
    connection.close()
    return str_

def dodaj_studenta(id_student,id_zespol,imie_st,nazw_st):
    #get id studenta
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "SELECT * FROM `student` WHERE `imie` ='"+ str(imie_st) + "' AND `nazwisko`='" + str(nazw_st) + "'"
    cursor.execute(retrive)
    rows = cursor.fetchall()

    id_st = rows[0][0]
    print(id_st)

    #sprawdz czy zespol nie jest pelny!

    retrive = "SELECT * FROM `zespolstudent` WHERE IdZespol =" + str(id_zespol)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    if(len(rows) >= 4):
        connection.commit()
        connection.close()
        return "pelna"

    #sprawdz czy student jest liderem!
    retrive = "SELECT * FROM `zespol` WHERE Id =" + str(id_zespol)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    id_lider = str(rows[0][2])
    if(id_lider != str(id_student)):
        connection.commit()
        connection.close()
        return "notlider"

    #dodaj studenta
    retrive = "INSERT INTO `zespolstudent` VALUES (NULL," + str(id_zespol) + "," + str(id_st) + ")"
    cursor.execute(retrive)
    connection.commit()
    connection.close()
    return "ok"


def dodaj_temat(id_student,id_zespol,id_temat):
    """

    :param id_student: id studenta
    :param id_zespol: id zespolu
    :param id_temat: id tematu
    :return:

    Nalezy sprawdzic w pierwszej kolejnosci czy student (id_student) jest liderem zespolu (tabela zespol),
    jesli jest to nalezy sprawdzic czy zespol nie posiada jiuz tematu (zobacz sobie co zwraca mysql gdy rekord jest NULL,
    jesli tak to update tego rekordu o id_tematu
    Po dodaniu nalezy zakutalizowac takze tabele temat (zmienic kolumne czyZajety na 1)
    Jesli cos jeszcze warto zobaczyc to sprawdz, sam temat który zostanie przeslany na pewno będzie "wolny"

    return: ok\t -> gdy jest ok
            error\tnie\tlider -> gdy to nie lider chce wybrac temat
            ... -> w jakims innym przypadku (wyniknie w trakcie pisania)

    """


    id_student = str(id_student)
    id_zespol = str(id_zespol)
    id_temat = str(id_temat)

    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    search_lider_sql = "SELECT * FROM zespol WHERE Id = " + id_zespol + " AND IdStudent = " + id_student
    cursor.execute(search_lider_sql)
    row_count = cursor.rowcount
    if row_count > 0:
            sprawdz_temat_sql = "SELECT * FROM zespol WHERE Id = " + id_zespol
            cursor.execute(sprawdz_temat_sql)
            records = cursor.fetchall()

            id_t = str(-1)
            for row in records:
                id_t = str(row[1])
                print(id_t)
                print(type(id_t))
            if id_t == "None":
                print("tu!")
                sql = "UPDATE zespol SET IdTemat = " + id_temat + " WHERE Id = " + id_zespol
                cursor.execute(sql)
                connection.commit()
                sql = "UPDATE temat SET czyZajety = '1' WHERE Id = " + id_temat
                cursor.execute(sql)
                connection.commit()
                connection.close()
                return "ok"
            else:
                return "posiadamtemat"


    return "nielider"

def wyswielt_temat(id_zespol):
    """

    :param id_zespol:
    :return: temat !
    """
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()

    retrive = "SELECT * FROM `zespol` WHERE Id=" + str(id_zespol)
    cursor.execute(retrive)
    rows = cursor.fetchall()
    str_ = ""
    if(rows[0][1] is not None):
        retrive = "SELECT * FROM `temat` WHERE Id= " + str(rows[0][1])
        cursor.execute(retrive)
        rows = cursor.fetchall()
        print(rows)
        for index in range(len(rows[0])):
            str_ += str(rows[0][index]) + "\t"
        print(str_)
        return str_
    else:
        connection.commit()
        connection.close()
        return "braktematu"


def usun_temat(id_student,id_zespol):
    """
    :param id_student: id studenta
    :param id_zespol:  id zespolu
    :return:

    Sprawdzic czy student jest liderem (zespol) oraz czy zespol posiada temat
    Jesli oba są spelnione, usunac temat z zespolu -> return "ok"
    jesli nei jest liderem -> return "nielider"
    jesli nie posiada tematu -> return "nietemat"

    """


    id_student = str(id_student)
    id_zespol = str(id_zespol)
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="zpi_baza_danych")
    cursor = connection.cursor()
    search_lider_sql = "SELECT * FROM zespol WHERE Id = " + id_zespol + " AND IdStudent = " + id_student
    cursor.execute(search_lider_sql)
    row_count = cursor.rowcount
    if row_count > 0:
            sprawdz_temat_sql = "SELECT * FROM zespol WHERE Id = " + id_zespol
            cursor.execute(sprawdz_temat_sql)
            records = cursor.fetchall()
            id_t = str(-1)
            for row in records:
                id_t = str(row[1])
            if id_t is None:
                return "nieposiadatemat"
            else:
                sql = "UPDATE zespol SET IdTemat = Null WHERE Id = " + id_zespol
                cursor.execute(sql)
                connection.commit()
                sql = "UPDATE temat SET czyZajety = '0' WHERE Id = " + id_t
                cursor.execute(sql)
                connection.commit()
                connection.close()
                return "ok"
    return "nielider"