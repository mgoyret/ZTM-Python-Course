from ctypes import sizeof


class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False,
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __del__(self):
        return "deleted"

    def __call__(self):
        return 'yes??'

    def __getitem__(self, i):
        return self.my_dict[i]

    def __sizeof__(self):
        return 'pesas mucho!'

    def __dir__(self):
        return 'dcba'

    def __format__(self):
        return 'cambiado'



action_figure = Toy('red', 0)
print('__str__():\t', action_figure.__str__())
print('__len():\t', len(action_figure))
print('__del__():\t', action_figure.__del__())
print('__call__():\t', action_figure())
print('__call__():\t', action_figure['name'])
print('__sizeof__():\t', action_figure.__sizeof__())
print('__dis__():\t', dir(action_figure))
print(action_figure.__format__())