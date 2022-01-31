def generatorFunction(num):
    for i in range(num):
        yield i


# for item in generatorFunction(100):
#     print(item)

# haciendo esto vemos que no genera una lista, si no un
# 'objeto generador' unico
obj = generatorFunction(100)

print(next(obj))
print(next(obj))

# 'yield' pausa la funcion, y next la reaunuda, devolviendo el valor actual de la funcion (el que esta al lado de yield)
# podemos usar next hasta que se llega al limite, y tenemos un Stopiteration Error