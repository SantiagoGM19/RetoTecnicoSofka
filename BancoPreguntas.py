from random import random
from ConexionBD import ConexionBD
from Pregunta import Pregunta


class BancoPreguntas:
    #en el diccionario preguntas el identificador es la categoria (1,2,3,4,5)
    #y elemento es un objeto pregunta
    __preguntas = {};
    
    def configurarPreguntas(self):
        conexionBD = ConexionBD()
        array_preguntas = conexionBD.obtenerPreguntas()
        
        for array_pregunta in array_preguntas:
            categoria = array_pregunta[0]
            enunciado = array_pregunta[1]
            opciones = [array_pregunta[2],array_pregunta[3],array_pregunta[4],array_pregunta[5]]
            opcionCorrecta = array_pregunta[6]
            pregunta = Pregunta()
            pregunta.actualizar_enunciado(enunciado)
            pregunta.actualizar_opciones(opciones)
            pregunta.actualizar_opcionCorrecta(opcionCorrecta)
            self.__preguntas[categoria] = pregunta
    
    def elegirPreguntaAleatoria(self, dificultad):
        preguntasRonda = []
        
        for categoria,pregunta in preguntas.items():
            if(categoria == dificultad):
                preguntasRonda.append(pregunta)
                
        numeroPregunta = random.randint(0,4)
        preguntaElegida = preguntasRonda[numeroPregunta]
        return preguntaElegida
    
    def obtenerPreguntas(self): return self.__preguntas
    
    
            
