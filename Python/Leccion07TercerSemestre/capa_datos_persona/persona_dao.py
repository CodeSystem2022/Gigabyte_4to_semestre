# from Tools.scripts.var_access_benchmark import C

from capa_datos_persona.Persona import Persona
from capa_datos_persona.conexion import Conexion
from capa_datos_persona.cursor_del_pool import CursorDelPool
from logger_base import log


class PersonaDAO:
    """
    DAO significa: Data Acces Object
    CRUD siginifica:
                    Create ->Insertar
                    Read -> Seleccionar
                    Update -> Actualizar
                    Delete -> Eliminar
    """

    _SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    # Definimos los metodos de la clase
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas = []  # creamos una lista
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Persona Insetada: {persona}')
            return cursor.rowcount
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.nombre, persona.apellido, persona.email,persona.id_persona)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            valores = (persona.id_persona,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Los objetos eliminaso son: {persona}')
            return cursor.rowcount



if __name__ == '__main__':

    #Eliminar un Registro
    persona1 = Persona(id_persona=18)
    personas_eliminadas =PersonaDAO.eliminar(persona1)
    log.debug(f'Personas eliminadas: {personas_eliminadas}')

    #Actualizar un regisro
    persona1 = Persona(1,'Jose','Pena','JPena@mail.com')
    persona_actualizadas = PersonaDAO.actualizar(persona1)
    log.debug(f'Personas acrualizadas: {persona_actualizadas}')

    # Insertar un registro
    persona1 = Persona(nombre='Marcelo', apellido='Torres', email='mtorres@mail.com')
    persona_insertadas = PersonaDAO.insertar(persona1)
    log.debug(f'Personas insertadas: {persona_insertadas}')

    # seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)
