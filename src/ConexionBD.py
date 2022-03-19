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
        try:
            query = ('SELECT categorias.nombre, categorias.dificultad, preguntas.enunciado, preguntas.opcion1,'
            'preguntas.opcion2, preguntas.opcion3, preguntas.opcion4, '
            'preguntas.correcta FROM preguntas '
            'JOIN categorias ON categorias.id = preguntas.id_categoria')
            self.cursor.execute(query)
            preguntas = self.cursor.fetchall()
            return preguntas

        except Exception as error:
            raise error
    
    def guardarJuego(self, jugador, rondaMaxima, acumulado, esFinalForzao):    
        try:
            idJugador = jugador.obtenerId()
            puntaje = jugador.obtenerPuntaje()
        
            queryJugador = 'UPDATE jugadores SET puntaje = {} where id = {} '.format(puntaje, idJugador)
        
            queryJuego = ('INSERT INTO juegos (id_jugador, rondaMaxima, puntajeMaximo, acumulado, finalForzado)'
                      'VALUES ({},{},{},{},{})'.format(idJugador, rondaMaxima, puntaje, acumulado, esFinalForzao)
                      )
            self.cursor.execute(queryJugador)
            self.cursor.execute(queryJuego)
        except Exception as error:
            raise error
    
    
