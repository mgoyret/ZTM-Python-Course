# para abrir archivos, hacer try exept, y escribir asi:
try:
    with open('/path/file.txt', mode='r') as myFile:
        pass
except FileNotFoundError as err:
    print('file not found')
'''
de esta manera, con el with as, no hace falta cerra el archivo. Cuando termina
lo que esta indentado dentro, se cierra
'''