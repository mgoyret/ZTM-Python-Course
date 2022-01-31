# Ejercicio 1
'''
Write a program which will find all such numbers which are
divisible by 7 but are not a multiple of 5, between 2000 and 3200
(both included).The numbers obtained should be printed in a
comma-separated sequence on a single line.
'''

from unittest import result


res = []
for num in range(2000, 3201):
    if not num % 7 and num % 5:
        res.append(num)
print(res)

res2 = [num for num in range(2000, 3201) if not num % 7 and num % 5]
print(res2)
