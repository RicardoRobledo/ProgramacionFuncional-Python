def funcion():
    x=1
    def interna():
        return x #closure porque el valor de 'x' queda capturado dentro de la funcion
    return interna


f = funcion()
print(f()==1)
print(f)
