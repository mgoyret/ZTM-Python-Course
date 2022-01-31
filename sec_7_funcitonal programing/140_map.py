# para multiplicar varios numeros seria asi
def multiply2(list):
    res = []
    for item in list:
        res.append(item*2)
    return res

# pero con map, reducimos a hacerlo de a uno, dandole cada dato


def multiply2_map(item):
    return item*2


# en el programa hacemos:
print(res_map := list(map(multiply2_map, [1, 2, 3])))

# no afecta la lista que damos como argumento a map(), si no que devuelve un mapa
# con los resultados en cada posicion, que lo pasamos a lista
