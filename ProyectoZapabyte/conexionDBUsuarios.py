import psycopg2 #adaptador de PostgreSQL para Python.

class ConexionDBUsuario:
    #constructor, se establece una conexión a la base de datos PostgreSQL
    def __init__(self):
        try:
            self.conexion = psycopg2.connect(
                host="localhost",
                database="proyecto_Python",
                user="postgres",
                password="admin"
            )
            self.crear_tabla()  # Llama al método crear_tabla al inicializar la conexión por si esta no existe
        except psycopg2.Error as e:
            print("Error al conectar a la base de datos:", e)

#Este método se encarga de crear una tabla llamada "comentarios" con columnas para "id", "nombre", "correo" y "mensaje"
    def crear_tabla(self): 
        cursor = self.conexion.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS comentarios (
                id SERIAL PRIMARY KEY,
                nombre TEXT,
                correo TEXT,
                mensaje TEXT
            )
            """
        )
        self.conexion.commit()

#Este método te permite insertar comentarios en la tabla "comentarios". Toma tres parámetros: nombre, correo y mensaje
    def insertar_comentario(self, nombre, correo, mensaje):
        cursor = self.conexion.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO comentarios (nombre, correo, mensaje)
                VALUES (%s, %s, %s)
                """,
                (nombre, correo, mensaje)
            )
            self.conexion.commit() #confirma los cambios, y si hay un error, revierte la transacción 
            print("Comentario insertado correctamente.")
        except psycopg2.Error as e:
            self.conexion.rollback()
            print("Error al insertar comentario:", e)
        finally:
            cursor.close()