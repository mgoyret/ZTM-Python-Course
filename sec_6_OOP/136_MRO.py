class A:
    char = 'a'


class B(A):
    char = 'b'


class C(A):
    char = 'c'


class D(B, C):
    pass

# mro() method resolucion order. Esta funcion nos muestra la jerarquia de como ve para arriba 'D'
print(D.mro())
