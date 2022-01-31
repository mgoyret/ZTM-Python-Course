def myDecorator(func):
    def wrapFunc(*args, **keyargs):
        print('boosting function')
        func(*args, **keyargs)
        print('***********\n')
    return wrapFunc


@myDecorator
def hello(param):
    print(param)


@myDecorator
def bye():
    print('bye')


mes = 'hellooooo'
hello(mes)
bye()
