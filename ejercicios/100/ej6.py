'''
Write a program that calculates and prints the value according to the given formula:
    Q = Square root of [(2_C_D)/H]
where:
    - C = 50
    - H = 30.
    - D = variable whose values should be input to your program in a comma-separated sequence

For example Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''
from math import sqrt

C, H = 50, 30
D = [float(num)
     for num in input('ingrese valores separados por coma: ').split(',')]

res = []
for i in D:
    res.append(int(sqrt((2*C*i)/H)))

print(res)
