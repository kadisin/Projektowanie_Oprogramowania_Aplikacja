import unittest
import database_methods


class UnitTests(unittest.TestCase):


    def test_example(self):
        data = [1,2,3]
        result = sum(data)
        self.assertEqual(result,6)


    def test_authorization(self):
        login = "example_login"
        password = "example_password"
        """
            check_account_in_database(login,password) return: (boolean,user(if exist))
        """
        self.assertTrue(database_methods.check_account_in_database(login,password)[0])

    def test_find_zespol_by_id_student(self):
        #example user and example zespol
        id_zespol = 100
        id_student = 9
        """
            find_zespol_by_id_student(id_student) return: (boolean,id_zespol(if exist))
        """
        self.assertEqual(database_methods.find_zespol_by_id_student(id_student)[1],str(id_zespol))

    def test_pokaz_moj_zespol(self):
        id_zespol = 100
        """
           pokaz_moj_zespol(id_zespol) return: "imie_1 nazwisko1\timie_2 nazwisko_2\t..." 
        """
        self.assertEqual(database_methods.pokaz_moj_zespol(id_zespol),"example_imie example_nazwisko\t")

    def test_check_free_topic(self):
        """
            check_free_topic() return: (boolean(if exist),list_of_free_topic)
        """
        self.assertTrue(database_methods.check_free_topic())

    def test_usun_osobe(self):
        """
            usun_osobe(id_student,id_zespol,imie_st_do_usuniecia,nazwisko_st_do_usuniecia) return:
            if wrong data -> error\t
            if id_student is not lider of id_zespol -> error\tlider\t
            if all good -> ok\t
        """
        id_student = -1
        id_zespol = -1
        imie_st_do_usuniecia = ""
        nazwisko_st_do_usuniecia = ""
        self.assertEqual(database_methods.usun_osobe(id_student,id_zespol,imie_st_do_usuniecia,nazwisko_st_do_usuniecia),"error\t")

if __name__ == '__main__':
    unittest.main()