# un decorador sobrecarga una funcion. Le 'potencia'

# esta es la manera en la que python reconoce un decorator
def myDecorator(func):
    def wrapFunc():
        print('boosting function')
        func()
        print('***********')
    return wrapFunc

@myDecorator
def hello():
    print('helloooooooooo')

hello()

# esto es analogo a hacer
hello2 = myDecorator(hello)
hello2()
# myDecorator toma nuestra funcion, y retorna el nombre
# de la nueva funcion que boosteo a la nuestra. Hello2 ahora vale
# ese retorno. Entonces, al hacerle call a hello2, sucede lo que vemos
# seria analogo tambien a hacer:
myDecorator(hello)()
# donde [myDecorator(hello)] = lo que retorna, que es el nombre de la wrap,
# y al llamar a esa wrap, sucede lo esperado

# ATENCION!!
# para los ultimos dos casos abria que sacar la definicion
# de hello() del decorador, ya que ya lo estamos haciendo manualmente,
# por eso queda doble el efecto