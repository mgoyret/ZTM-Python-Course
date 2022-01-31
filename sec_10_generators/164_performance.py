# usar generadores es mucho mas rapido, porque usa menos recursos
# verificamos:
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
def long_time():
    print('con generador:')
    for i in range(100000000):
        i*5


@performance
def long_time2():
    print('sin generador:')
    for i in list(range(100000000)):
        i*5


long_time()
long_time2()
