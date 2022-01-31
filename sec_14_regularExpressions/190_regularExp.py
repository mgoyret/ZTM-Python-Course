import re

pattern = re.compile((r'([a-z])([A-Z])'))
string = 'holA yo soY Marcos'

a = pattern.findall(string)
b = pattern.search(string)
c = b.group(1)
print(a)
print(b)
print(c)
'''
group me muestra de lo que se encontro, cual pertenece al grupo 1.
Es la l, porque la secuencia lo que busca es donde hay una minuscula seguida
de una mayuscula, y es en el [lA]
'''

