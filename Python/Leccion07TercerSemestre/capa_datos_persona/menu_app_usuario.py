from capa_datos_persona.Usuario import Usuario
from capa_datos_persona.usuario_dao import UsuarioDao
from logger_base import log

opcion = None
while opcion !=5:
    print('Opciones')
    print('1.Listar usuarios')
    print('2.Agregar usuarios')
    print('3.Modificar usuarios')
    print('4.Eliminar usuario')
    print('5.Salir')
    opcion = int(input("Eliga una opcion (1-5): "))
    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif opcion ==2:
        username_var = input('Digite el nombre de usuario: ')
        password_var = input('Digite su contrasena: ')
        usuario = Usuario(username=username_var,password=password_var)
        usuario_insertado = UsuarioDao.insertar(usuario)
        log.info(f'Usuario insertado: {usuario_insertado}')
    elif opcion ==3:
        id_usuario_var = int(input('Digite la id del usuario a modificar: '))
        username_var = input('Digite el nombre de usuario a modficar: ')
        password_var = input('Digite la contrasena del usuario modificado: ')
        usuario = Usuario(id_usuario=id_usuario_var, username=username_var, password=password_var)
        usuario_actualizado = UsuarioDao.actualizar(usuario)
        log.info(f'Usuario actualizado: {usuario_actualizado}')
    elif opcion ==4:
        id_usuario_var = int(input('Digite la id del usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario_var)
        usuario_eliminado = UsuarioDao.eliminar(usuario)
        log.info(f'Usuario eliminado :{usuario_eliminado}')
else:
    log.info('Salimos de la aplicacion,hasta pronto!!!')