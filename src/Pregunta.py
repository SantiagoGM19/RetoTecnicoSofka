class Pregunta:
    __enunciado = ""
    __opciones = []
    __opcionCorrecta = None
    __dificultad = 0
    __categoria = ""
    
    def obtenerEnunciado(self): return self.__enunciado
    
    def obtenerOpciones(self): return self.__opciones
    
    def obtenerOpcionCorrecta(self): return self.__opcionCorrecta
    
    def obtenerDificultad(self): return self.__dificultad
    
    def obtenerCategoria(self): return self.__categoria
    
    def actualizarEnunciado(self, enunciado): self.__enunciado = enunciado
    
    def actualizarOpciones(self, opciones): self.__opciones = opciones
    
    def actualizarOpcionCorrecta(self, opcionCorrecta): self.__opcionCorrecta = opcionCorrecta
    
    def actualizarDificultad(self, dificultad): self.__dificultad = dificultad
    
    def actualizarCategoria(self, categoria): self.__categoria = categoria
    