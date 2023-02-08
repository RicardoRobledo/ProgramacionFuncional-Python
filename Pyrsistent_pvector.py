def actualizar(lista, valor):
    nueva = lista[:]
    nueva[-1] = valor
    return nueva

miLista = [1,2,3]
nl = actualizar(miLista, 5)
print(nl)
print(miLista)


from pyrsistent import pvector, v

vec = pvector([1,2,3]) # transformamo una lista a un vector
vec2 = v(1,2,3) # tambien lo podemos hacer mediante 'v'

print(vec[2])
print(vec2[0])


print(vec.append(4))
print(vec)

r = vec2.append(5)
print(r)
print(vec2)


print(vec.set(0, 11))
print(vec)

r = vec2.set(0, 11)
print(r)
print(vec2)
