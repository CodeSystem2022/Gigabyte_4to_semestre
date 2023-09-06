
#Bool contiene los valores de True y False
#Los tipos numericos es false para el 0(cero), y true para los demas valores
valor = 0
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

valor = 15
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

valor = -1
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

valor = 0.1
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')


#Tipo string ->False '', True para los demas valores
valor = ''
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

valor = 'hola'
resultado = bool(valor)
print(f'Valor: {valor}, resultado: {resultado}')

#Tipo de colecciones -> False para colecciones vacias
#Tipo de colecciones -> True para las demas
valor = []
resultado = bool(valor)
print(f'Valor de una lista vacia: {valor}, resultado: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'Valor de una lista con elementos: {valor}, resultado: {resultado}')

#Tupla
valor = ()
resultado = bool(valor)
print(f'Valor de una tupla vacia: {valor}, resultado: {resultado}')

valor = (5,)
resultado = bool(valor)
print(f'Valor de una tupla con elementos: {valor}, resultado: {resultado}')

#Diccionario

valor = {}
resultado = bool(valor)
print(f'Valor de un diccionario vacio: {valor}, resultado: {resultado}')
valor = {'Nombre':'Juan','Apellido':'Perez'}
resultado = bool(valor)
print(f'Valor de un diccionario con elementos: {valor}, resultado: {resultado}')

#Setencias de control con bool
if'':
    print("Regresa verdadero")
else:
    print('Regresa falso')


if bool('hola'):
    print("Regresa verdadero")
else:
    print('Regresa falso')

if 15:
    print("Regresa verdadero")
else:
    print('Regresa falso')

if valor:
    print("Regresa verdadero")
else:
    print('Regresa falso')

# ciclos
variables = 0
while variables:
    print('regresa verdadero')
    break
else:
    print('Regresa falso')


