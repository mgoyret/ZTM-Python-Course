'''
Write a program which accepts a sequence of comma separated 4 digit binary
numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
'''

inp = list(input('enter coma sep. 4 digit binary numbers: ').split(','))
inp = [int(num, 2) for num in inp]

print( res := list(filter(lambda item: item%5 == 0, inp)) )