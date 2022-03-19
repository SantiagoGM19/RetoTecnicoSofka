from BancoPreguntas import BancoPreguntas
from ConexionBD import ConexionBD
from Jugador import Jugador


class Ronda:

    __acumulado = 0
    __nivelDificultad = 1
    __jugador = None

    def definirJugador(self, nombre):
        self.__jugador = Jugador()
        self.__jugador.registrarNombre(nombre)
        print("Bienvenido jugador ", self.__jugador.obtenerNombre(),
              "Buena suerte en tu juego")

    def configurarJuego(self):
        bancoPreguntas = BancoPreguntas()
        bancoPreguntas.configurarPreguntas()
        return bancoPreguntas

    def iniciarJuego(self):
        bancoPreguntas = self.configurarJuego()
        preguntaRonda = bancoPreguntas.elegirPreguntaAleatoria(self.__nivelDificultad)
        enunciado = preguntaRonda.obtenerEnunciado()
        opciones = preguntaRonda.obtenerOpciones()
        opcionCorrecta = preguntaRonda.obtenerOpcionCorrecta()
        categoria = preguntaRonda.obtenerCategoria()
        pregunta = [enunciado, opciones, opcionCorrecta, categoria]
        return pregunta

    def responderPregunta(self, opcionRespondida, opcionCorrecta):
        if(opcionRespondida == opcionCorrecta):
            self.aumentarNivel()
        else:
            print("Incorrecto! Pierdes la ronda y pierdes el premio acumulado")
            self.__acumulado = 0
            self.terminarRonda(True)

    def aumentarNivel(self):
        if(self.__nivelDificultad == 5):
            print("Felicidades jugador ", self.__jugador.obtenerNombre(),
                  "has logrado terminar la última ronda, tu puntaje es: ",
                  self.__jugador.obtenerPuntaje())
            self.terminarRonda(False)
        else:
            self.__nivelDificultad += 1
            factor = self.__nivelDificultad + 1
            self.__jugador.aumentarPuntaje(factor)
            self.acumularPremio()
            print("Correcto! Siguiente ronda")

    def acumularPremio(self): self.__acumulado = self.__jugador.obtenerPuntaje()

    def terminarRondaVoluntario(self):
        print("Felicidades jugador ", self.__jugador.obtenerNombre(),
              " te retiras con ", self.__acumulado, " puntos")
        terminarRonda(False)
        
    def terminarRonda(self, esFinalForzado):
        conexionBD = ConexionBD()
        conexionBD.guardarJuego(self.__jugador, self.__nivelDificultad, self.__acumulado, esFinalForzado)

    def obtenerAcumulado(self): return self.__acumulado

    def obtenerNivelDificultad(self): return self.__nivelDificultad
