################## list comprehension

# para crear una lista en base a un iterable, en lugar de
# list1 = []
# for char in [iterable]:
#     list1.append(char)

list1 = [char for char in 'hello']
list2 = [num for num in (range(100))]
print('list1:\t', list1, '\n')
print('list2:\t', list2, '\n')

# lo que ponemos antes de 'for' es lo que se agrega. En lugar de ser directamente
# el elemento del iterable, puede ser una expresion...
list3 = [num**2 for num in range(100)]
print('list3:\t', list3, '\n')

# expandiendo, para crear lista solo con los pares de list3:
list4 = list(filter(lambda item: item %
             2 == 0, [num**2 for num in range(100)]))
# o mas facil:
list4 = [num**2 for num in range(100) if num % 2 == 0]
print('list4:\t, ', list4, '\n')


################## set comprehension

# igual, pero
set1 = {num**2 for num in range(100) if num % 2 == 0}

################## dict comprehension
simpleDict = {
    'a': 1,
    'b': 2
}
dict1 = {k: v**2 for k,v in simpleDict.items()}
print('dict1:\t', dict1, '\n')

# Ej: armar dict con clave que sea el numero de una lsita, y valor el numero al cuadrado
dict2 = {num:num*2 for num in [1, 2, 3]}
print('dict2:\t', dict2, '\n')