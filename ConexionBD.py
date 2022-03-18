import pymysql


class ConexionBD:

    def __init__(self):

        error_mysql = pymysql.err
        
        try:
            self.conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='concurso_preguntas'
            )
            self.cursor = self.conexion.cursor()

        except (error_mysql.OperationalError, ConnectionRefusedError):
            print("Error conectando con la base de datos"
                  "posible rechazo de conexión, revisar y luego intentar de nuevo")

    def obtenerPreguntas(self):

        query = ('SELECT categorias.nombre, preguntas.enunciado, preguntas.opcion_1, '
                'preguntas.opcion_2, preguntas.opcion_3, preguntas.opcion_4, '
                'preguntas.correcta FROM preguntas '
                'JOIN categorias ON categorias.id = preguntas.id_categoria')

        try:
            self.cursor.execute(query)
            preguntas = self.cursor.fetchall()
            return preguntas

        except Exception as error:
            raise error
