def adiciona(lista):
    lista.append('manzana')
    return lista

miLista = ['pera', 'banana']
print(adiciona(miLista))
print(miLista)


def adiciona2(lista):
    return lista+['manzana']

miLista = ['pera', 'banana']
print(adiciona2(miLista))
print(miLista)


a = {'hola':'amigos'}
b = {'saludos':'coders'}

c = a.copy()
c.update(b)
print(c,a,b)
