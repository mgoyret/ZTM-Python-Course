from random import randint
from sys import argv
import pdb

inp = 0
randNum = randint(int(argv[1]), int(argv[2]))
pdb.set_trace()
if int(argv[1]) < 1:
    print('ingrese limite inferior mayor a [0]')
else:
    print(f'Adivine el numero aleatorio entre {argv[1]} y {argv[2]}, o ingrese \'-1\' para finalizar\n')
    while True:
        try:
            inp = int(input('ingrese: '))
            if int(argv[1]) <= inp <= int(argv[2]):
                if inp != randNum:
                    if inp == -1: break
                    print('numero incorrecto!')
                    continue
                else:
                    print('CORRECTO!!!!!', randNum)
                    break
            else:
                print(f'Betwen {argv[1]}--{argv[2]}')
        except ValueError:
            print('Please enter a number')
            continue
    print('ADIOS!')
