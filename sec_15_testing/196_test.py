import unittest
import main


class TestGame(unittest.TestCase):
    def setUp(self):
        print('about to run a function, setting variables and conf')

    def tearDown(self):
        print('finishing function, cleanning up')

    def test_input(self):
        '''comentario 1'''
        result = main.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = main.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.run_guess(5, '11')
        self.assertFalse(result)
# que solo se corran las funciones si este es el archivo ejecutado


if __name__ == '__main__':
    unittest.main()

'''
unittest nos da assert methods para probar cosas que verifiquen mis funciones

ATENCION los archivos van al revez, main es test y test es main
pero estan asi poorque el test si o si corre el main.py


para correr un archivo test, se hace >>python3 unittest,
pero para correr muchos a la vez, es >>python3 -m unittest
Con '-v'hacemos que nos muestre cada funcion que prueba, y
muestra los comentarios dentro de cada funcion
metodo: def setUp(self):
  pass
corre eso antes de cada funcion. Sirve para establecer variables y cosas asi
contraria a esa, esta: def tearDown(self): para cuando
termina cada funcion
'''
