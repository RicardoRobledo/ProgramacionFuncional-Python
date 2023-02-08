def incrementa(f, numeros):
    if numeros==[]:
        return []
    else:
        return [f(numeros[0])] + incrementa(f, numeros[1:])

valor_agregacion = 2
print(incrementa(lambda n: n+valor_agregacion, [1,2,3]))


def conteo(lista):
    if lista==[]:
        return 0
    else:
        return 1 + conteo(lista[1:])

def sumatoria(lista):
    if lista==[]:
        return 0
    else:
        return lista[0] + sumatoria(lista[1:])

def conteoSuma(f, lista):
    if lista==[]:
        return 0
    else:
        return f(lista[0]) + conteoSuma(f, lista[1:])

print(f'Conteo: {conteoSuma(lambda _:1, [1,2,3,4])}')
print(f'Sumatoria: {conteoSuma(lambda n:n, [1,2,3,4])}')


def mayor(numeros, mayorActuAl=0):
    if numeros==[]:
        return mayorActuAl
    else:
        if numeros[0]>mayorActuAl:
            mayorN = numeros[0]
        else:
            mayorN = mayorActuAl

    return mayor(numeros[1:], mayorN)

print(mayor([1,5,11,7,4,9,6]))


def reducida(f, lista, acc):
    if lista==[]:
        return acc
    else:
        accN=f(lista[0], acc)
        return reducida(f, lista[1:], accN)

def mayor(lista):
    return reducida(lambda num, acc: num if num>acc else acc, lista, 0)

def conteo(lista):
    return reducida(lambda _, acc: acc+1, lista, 0)

def sumatoria(lista):
    return reducida(lambda num, acc: num+acc, lista, 0)

def mapeo(f, lista):
    return reducida(lambda el, acc: acc+[f(el)], lista, [])

def incrementa1(lista):
    return mapeo(lambda n:n+1, lista)

print(f'Mayor {mayor([3, 4, 2, 1, 1])}')
print(f'Conteo {conteo([3, 4, 2, 1, 1])}')
print(f'Sumatoria {sumatoria([3, 4, 2, 1, 1])}')
print(incrementa1([3,4,2,1,1]))


def reducida2(f, lista, acc):
    for el in lista:
        acc=f(el,acc)
    return acc

def mayor2(lista):
    return reducida2(lambda num, acc: num if num>acc else acc, lista, 0)

def conteo2(lista):
    return reducida2(lambda _, acc: acc+1, lista, 0)

def sumatoria2(lista):
    return reducida2(lambda num, acc: num+acc, lista, 0)

def mapeo2(f, lista):
    return reducida2(lambda el, acc: acc+[f(el)], lista, [])

def incrementa12(lista):
    return mapeo2(lambda n:n+1, lista)

print(f'Mayor {mayor2([3, 4, 2, 1, 1])}')
print(f'Conteo {conteo2([3, 4, 2, 1, 1])}')
print(f'Sumatoria {sumatoria2([3, 4, 2, 1, 1])}')
print(incrementa12([3,4,2,1,1]))


'''
def incrementa(x):
    r = x+5
    return r

def f1(x):
    r = f2(x)+f3(x)
    print(r)
    return r

def f2(x):
    r = x*2
    print(r)
    return r

def f3(x):
    r = x-5
    print(r)
    return r

f1(10)
'''


'''def calcular(f, val):
    return f(val)

def f1(x):
    return calcular(lambda x:f2(x)+f3(x), x)

def f2(x):
    return calcular(lambda x:x*2, x)

def f3(x):
    return calcular(lambda x:x-5, x)


print(f1(2))
print(f2(2))
print(f3(2))
'''


def calcular(f):
    return lambda x: f(x)

@calcular
def f1(x):
    return f2(x)+f3(x)

@calcular
def f2(x):
    return x*2

@calcular
def f3(x):
    return x-5


print(f1(2))
print(f2(2))
print(f3(2))
