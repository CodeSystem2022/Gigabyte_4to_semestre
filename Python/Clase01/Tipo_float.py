#profundizamos en el tipo float
a = 3.0
print(f'a = {a:.8f}')

#Constructor de tipo float -> puede recibir int y str
a = float(10) #Le pasamos un numero entero  (int)
print(f'a = {a:.2f}')

a = float("23")
print(f'a = {a:.1f}')

#Notacion exponencial (valores positivos o negativos)
a= 3e5
print(f'a = {a}')
a= -3e5
print(f'a = {a}')
a= 3e-5
print(f'a = {a:.6f}')

#Cualquier calculo que incluye un float, todo cambia a float
a = 4.0 +5
print(f'a = {a}')
print(f'a = {type(a)}')

