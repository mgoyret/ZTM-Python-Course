# funcion que filtra y devuelve menos de lo que le damos (a veces)

nums = [1, 2, 3]

def onlyOdd(item):
    return item%2 != 0

#filter solo devuelve los parametros que dan True
print( resOdds := list(filter(onlyOdd, nums)) )