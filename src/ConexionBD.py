import pymysql


class ConexionBD:

    def __init__(self):

        self.error_mysql = pymysql.err
        self.incremento_idJugador = 0
        try:
            self.conexion = pymysql.connect(
                host='localhost',
                user='root',
                password='',
                db='concurso_preguntas'
            )
            self.cursor = self.conexion.cursor()

        except (self.error_mysql.OperationalError, ConnectionRefusedError):
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
    
    def registrarJugador(self, jugador):
        try:
            nombreJugador = jugador.obtenerNombre()
            puntajeJugador = jugador.obtenerPuntaje()
            nickName = jugador.obtenerNickName()
            comprobacion = self.verificarJugador(nickName)
            if(comprobacion):
                print("\nEl nickName ya se encuentra registrado\n")
                return True
            else:
                queryJugador = ("INSERT INTO jugadores (nickName, nombre, puntaje)"
                                "VALUES ('{}','{}','{}')".format(nickName, nombreJugador, puntajeJugador))
                self.cursor.execute(queryJugador)
                self.conexion.commit()
        except Exception as error:
            print("ERROR: No se pudo registrar el jugador correctamente")
            raise error
    

    def guardarJuego(self, jugador, rondaMaxima, acumulado, esFinalForzao):    
        try:
            nickName = jugador.obtenerNickName()
            puntaje = jugador.obtenerPuntaje()
        
            queryJugador = "UPDATE jugadores SET puntaje = {} where nickName = '{}' ".format(puntaje, nickName)
        
            queryJuego = ("INSERT INTO juegos (nickNameJugador, rondaMaxima, puntajeMaximo, acumulado, finalForzado)"
                      "VALUES ('{}',{},{},{},{})".format(nickName, rondaMaxima, puntaje, acumulado, esFinalForzao)
                      )
            self.cursor.execute(queryJugador)
            self.cursor.execute(queryJuego)
            self.conexion.commit()
        except Exception as error:
            print("ERROR: No se ha podido registar el juego correctamente")
            raise error
    
    def verificarJugador(self, nickName):
        try:
            query = "SELECT nickName FROM jugadores WHERE nickName = '{}'".format(nickName)
            self.cursor.execute(query)
            resultado = self.cursor.fetchall()
            if(len(resultado) == 0):
                return False
            else:
                if (resultado[0][0] == nickName):
                    return True
        except Exception as error:
            raise error
    
    
