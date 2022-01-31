# En su momento, hicimos esta resolucion para hallar duplicados:

someList = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = []
# for value in someList:
#     if someList.count(value) > 1 and not duplicates.count(value):
#         duplicates.append(value)
# print(duplicates)

# ahora, en una linea con comprehension: lo hago set para no crear duplicados
duplicates = list({x for x in someList if someList.count(x) > 1})
print(duplicates)
