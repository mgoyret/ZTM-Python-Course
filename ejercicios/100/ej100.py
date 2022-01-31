'''
You are given words. Some words may repeat. For each word, output its
number of occurrences. The output order should correspond with the input
order of appearance of the word. See the sample input/output for clarification.
'''

words = dict()
while True:
    if (aux := input('ingrese una palabra, o \"end\" para terminar: ')) == 'end':
        break
    elif list(words.keys()).count(aux):
        words.update({aux: words[aux] + 1})
    else: words.update({aux: int(1)})

print( res := list(words.values()) )