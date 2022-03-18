class Pregunta:
    #opciones es un diccionario con 4 opciones donde el identificador es un 1 o un 0
    #solo habrá una opción con identificador 1 para saber que es la opción correcta
    __enunciado = None
    __opciones = None
    __opcionCorrecta = None
    
    def obtenerEnunciado(self): return self.__enunciado
    
    def obtenerOpciones(self): return self.__opciones
    
    def obtenerOpcionCorrecta(self): return self.__opcionCorrecta
    
    def actualizar_enunciado(self, enunciado): self.__enunciado = enunciado
    
    def actualizar_opciones(self, opciones): self.__opciones
    
    def actualizar_opcionCorrecta(self, opcionCorrecta): self.__opcionCorrecta = opcionCorrecta
    