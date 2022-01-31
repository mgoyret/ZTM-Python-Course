# Ejercicio 4
'''
Write a program which accepts a sequence of comma-separated numbers
from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program: 34,67,55,33,12,98
'''

l1 = input('Ingrese: ').split(',')
l1 = [float(num) for num in l1]
t1 = tuple(l1)
print(f'list:\t{l1}\ntuple:\t{t1}')

print(type(l1[0]))
