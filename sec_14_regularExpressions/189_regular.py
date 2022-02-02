'''
VER:
https://www.w3schools.com/python/python_regex.asp
https://regex101.com/

lockbehind ahead
https://www.regular-expressions.info/lookaround.html
'''

import re

string = 'hola esto es un string que empieza con hola'
a = re.search('hola', string)
b = re.match('hola', string)
c = re.fullmatch('hola', string)
d = re.fullmatch('hola esto es un string que empieza con hola', string)
e = re.findall('hola', string)

'''
las funciones regulares son muy utiles. En este caso, vemos algunas que sirven 
podemos hacer lo siguiente:
'''

pattern = re.compile('hola')
f = pattern.search(string)
g = pattern.findall(string)

print(f'a: {a}', f'b: {b}', f'c: {c}', f'd: {d}',
    f'e: {e}', f'f: {f}', f'g: {g}', sep='\n')