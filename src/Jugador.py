class Jugador:
    
    __nickName = 0
    __nombre = None
    __puntaje = 0
    
    def obtenerNombre(self): return self.__nombre
    
    def registrarNombre(self, nombre): self.__nombre = nombre
    
    def obtenerPuntaje(self): return self.__puntaje
    
    def aumentarPuntaje(self, factor): self.__puntaje += 100*factor
    
    def obtenerNickName(self): return self.__nickName
    
    def registrarNickName(self, nickName): self.__nickName = nickName
    
    
    