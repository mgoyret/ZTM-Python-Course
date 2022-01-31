# funciones anonimas, que se usan solo una vez y se destruyen
# Al terminar su ejecucion, no quedan guardadas en memoria

from functools import reduce
list1 = [1, 2, 3]
print('list1:\t\t', list1)
# ejemplo map

# def multiply2_map(item):
#     return item*2
# en lugar de armar esta funcion para un uso, y que quede en memoria, hacemos
# lo siguiente:
# lambda [param]: action -> resultado de la action


resMap = list(map(lambda item: item*2, list1))
print('map():\t\t', resMap)

# ejemplo filter

# def onlyOdd(item):
#     return item%2 != 0
# print( resOdds := list(filter(onlyOdd, list1)) )

resFilter = list(filter(lambda item: item % 2 != 0, list1))
print('filter():\t', resFilter)


# ejemplo reduce

# def accumulator(acc, item):
#     return acc + item
# print( res := reduce(accumulator, list1, 0) )

resReduce = reduce(lambda acc, item: acc+item, list1, 0)
print('reduce():\t', resReduce)
