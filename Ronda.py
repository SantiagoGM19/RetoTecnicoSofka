from Jugador import Jugador


class Ronda:
    
    def __init__(self):
        self.acumulado = 0
        self.nivelDificultad = 1
        self.jugador = None
        self.nombreJugador = None
        
    
    def definirJugador(self, nombre):
        self.jugador = Jugador(nombre)
        self.nombreJugador = self.jugador.obtenerNombre()
        print("Bienvenido jugador ", self.nombreJugador, "Buena suerte en tu juego")
        
    def aumentarNivel(self):
        if(self.nivelDificultad == 5):
            print("Felicidades jugador ", self.nombreJugador, 
                  "has logrado terminar la última ronda, tu puntaje es: ", 
                  self.jugador.puntaje)
        else:
            self.nivelDificultad += 1
            self.jugador.aumentarPuntaje()
            self.acumulado = self.jugador.obtenerPuntaje()