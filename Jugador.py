class Jugador:
    
    __nombre = None
    __puntaje = 0
    
    def obtenerNombre(self): return self.__nombre
    
    def registrarNombre(self, nombre): self.__nombre = nombre
    
    def obtenerPuntaje(self): return self.__puntaje
    
    def aumentarPuntaje(self): self.__puntaje += 100
    
    