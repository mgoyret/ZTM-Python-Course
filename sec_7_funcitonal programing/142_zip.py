#le damos varios iterables, y forma parejas juntando los elementos de mismo index
list1 = [1, 2]
list2 = [11, 22, 33]
list3 = [111, 222, 333, 444]
print( list(zip(list1, list2, list3)) )
#la longitud del zip es la de la minima lista