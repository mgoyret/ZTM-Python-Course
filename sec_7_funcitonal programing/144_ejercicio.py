from functools import reduce
from itertools import accumulate

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capitalizeStr(item):
    return item.capitalize()
print(my_pets := list(map(capitalizeStr, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]
print( zipList := list(zip(my_strings, sorted(my_numbers))) )

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def isPercentil50(percentage):
    return percentage > 50
print(res := list(filter(isPercentil50, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print( res := reduce(accumulator, scores + my_numbers, 0) )
