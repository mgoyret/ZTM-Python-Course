from decimal import DivisionByZero


while True:
    try:
        age = int(input('what is your age: '))
        print(age)
    except ValueError as err:
        print(f'Error: {err}\nplease enter a number')
    else:
        print('thanks!')
        break
 # podria captar muchos errores en una misma excepcion, con comas

while True:
    try:
        res = 3 / (op := int(input('Dividamos \'3\' por: ')))
    except (ValueError, ZeroDivisionError) as err:
        print(f'oops!\nError: {err}')
        continue  # reinicia loop
    except:  # other error
        raise Exception('other error')
    else:
        print(f'3 / {op} = {res}')
        break
    finally:
        print('cargar en log file')
    print('loop completo')
print('END\n')

# el finally corre siempre, haya o no error. Sirve por ejemplo
# en un box de inicio de sesion, para registrar todos los intentos,
# con o sin error

# raise lo que hace es forzar mensaje que digamos, con el codigo
# de error que especifiquemos
