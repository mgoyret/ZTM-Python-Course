'''
Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:

hello world! 123
Then, the output should be:

LETTERS 10
DIGITS 3
'''

let, dig = 0, 0
sentence = input('ingrese una oracion: ')
for char in sentence:
    if char.isalpha(): let += 1
    elif char.isnumeric(): dig += 1
print(f'LETTERS:\t{let}\nDIGITS:\t\t{dig}')
