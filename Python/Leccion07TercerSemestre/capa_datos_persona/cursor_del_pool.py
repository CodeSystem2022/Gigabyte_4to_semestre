from logger_base import log
from conexion import Conexion


class CursorDelPool:
    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        log.debug('Inicio del metodo with y __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    def __exit__(self, tipo_excepcion, valor_excepcion, detalle_excepcion):
        log.debug('Se ejecuta el metodo __exit__')
        if valor_excepcion:
            self._conexion.rollback()
            log.debug(f'Ocurrio una excepcion; {valor_excepcion}')
        else:
            self._conexion.commit()
            log.debug('Comit de la transaccion')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == "__main__":
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute("SELECT * FROM persona")
        log.debug(cursor.fetchall())
