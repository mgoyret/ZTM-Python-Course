'''
Write a program that accepts sequence of lines as input and prints
the linesafter making all characters in the sentence capitalized.

Suppose the following input is supplied to the program:
    - Hello world
    - Practice makes perfect

Then, the output should be:
    - HELLO WORLD
    - PRACTICE MAKES PERFECT
'''

inp = list()
while True:
    aux = input('Ingrese linea o \'end\' para terminar: ')
    if aux != 'end':
        inp.append(aux)
    else:
        break
for item in inp:
    print(item.upper())
