# Ej 1: square list
list1 = [5, 4, 3]
resSquare = list(map(lambda item: item**2, list1))
print(resSquare)

# Ej 2: sort en base a segundo valor del tuple
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda item: item[1])
print(a)
# .sort() si damos como argumento una funcion, ordena en base al
# resultado de la funcion
