# hay que importar esta funcion de la 'biblioteca' functools
from functools import reduce

def accumulator(acc, item):
    return acc + item

list1 = [1, 2, 3]

print( res := reduce(accumulator, list1, 0) )

#aca la usamos para reducir una lista a la suma de los elementos, pero tiene mas usos