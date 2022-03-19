class Jugador:
    
    __id = 0
    __nombre = None
    __puntaje = 0
    
    def obtenerNombre(self): return self.__nombre
    
    def registrarNombre(self, nombre): self.__nombre = nombre
    
    def obtenerPuntaje(self): return self.__puntaje
    
    def aumentarPuntaje(self, factor): self.__puntaje += 100*factor
    
    def obtenerId(self): return self.__id
    
    def registrarId(self, id): self.__id = id
    
    
    