'''
Write a program, which will find all numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

from time import time


def performance(fn):
    def wrapper(*args, **kawrgs):
        t1 = time()
        result = fn(*args, **kawrgs)
        t2 = time()
        print(f'took {t2-t1} s')
        return result
    return wrapper


@performance
def op1():

    numList = [str(num) for num in range(100, 300100)]
    res1 = list(filter(lambda num: all(ord(i) % 2 == 0 for i in num), numList))


'''
    La funcion ord() devuelve el unicode de un caracter dado. Yo habia hecho int(), y ver
    si era par, pero se ve que ord() es mucho mas rapida que int(). El unicode de cada
    numero no es el mismo numero, pero la paridad coincide, asique sirve para este caso.
'''
