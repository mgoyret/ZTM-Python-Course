def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


num = 25
j = 0
for i in fib(num):
    print(f'[{j}]', i)
    j += 1
