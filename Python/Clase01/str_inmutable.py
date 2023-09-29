#help(str.capitalize)
mensaje1 = 'Hola mundo'
mensaje2 = mensaje1.capitalize()
print(f'mensaje 1: {mensaje1}, id: {id(mensaje1)}')
print(f'mensaje 2: {mensaje2}, id: {id(mensaje2)}')

mensaje1 += 'adios'
print(f'mensaje 1: {mensaje1}, id: {id(mensaje1)}')