# Ejercicio 2
'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a
single line.Suppose the following input is supplied to the program:
8 Then, the output should be:40320
'''


def factorial(num) -> str:
    res = 1
    for i in range(1, num+1):
        res *= i
    return res


while True:
    try:
        num = int(input('calcular factorial de: '))
        if num < 0: raise ValueError
    except ValueError as err:
        print(f'Error: {err}\nplease enter a natural number')
    else:
        print(list(str(factorial(num))))
        break


#def shortFact(x): return 1 if x <= 1 else x*shortFact(x-1)
