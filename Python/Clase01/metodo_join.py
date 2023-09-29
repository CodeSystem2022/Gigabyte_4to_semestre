


#help(str.join)

tupla_str = ('Hola','alumnos','tecnicatura','universitaria')
mensaje = ' '.join(tupla_str)
print(f"mensaje: {mensaje}")

lista_cursos = ['Java','Python','Angular','Spring']
mensaje = ', '.join(lista_cursos)
print(f'Mensaje: {mensaje}')

cadena = 'Hola mundo'
mensaje = '.'.join(cadena)
print(f'Mensaje: {mensaje}')

diccionario  = {'nombre':'Juan','Apellido':'Pere','edad':'18'}
llaves ='-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'LLaves: {llaves}, Type: {type(llaves)}')
print(f'LLaves: {valores}, Type: {type(valores)}')