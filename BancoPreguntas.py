import random
from ConexionBD import ConexionBD
from Pregunta import Pregunta


class BancoPreguntas:
    #en el diccionario preguntas el identificador es la categoria (1,2,3,4,5)
    #y elemento es un objeto pregunta
    __preguntas = [];
    
    def configurarPreguntas(self):
        conexionBD = ConexionBD()
        array_preguntas = conexionBD.obtenerPreguntas()
        for array_pregunta in array_preguntas:
            categoria = array_pregunta[0]
            dificultad = array_pregunta[1]
            enunciado = array_pregunta[2]
            opciones = [array_pregunta[3],array_pregunta[4],array_pregunta[5],array_pregunta[6]]
            print(opciones)
            opcionCorrecta = array_pregunta[7]
            pregunta = Pregunta()
            pregunta.actualizarEnunciado(enunciado)
            pregunta.actualizarOpciones(opciones)
            pregunta.actualizarOpcionCorrecta(opcionCorrecta)
            pregunta.actualizarCategoria(categoria)
            pregunta.actualizarDificultad(dificultad)
            self.__preguntas.append(pregunta)
            # if(categoria in self.__preguntas):
            #     preguntasCategoria = self.__preguntas.get(categoria)
            #     preguntasCategoria.append(pregunta)
            #     self.__preguntas[categoria] = preguntasCategoria
            # else:
            #     self.__preguntas[categoria] = [pregunta]
                  
    def elegirPreguntaAleatoria(self, dificultad):
        preguntasRonda = []
        for pregunta in self.__preguntas:
            if(pregunta.obtenerDificultad() == dificultad):
                preguntasRonda.append(pregunta)
        numeroPregunta = random.randint(0,4)
        preguntaElegida = preguntasRonda[numeroPregunta]
        print(preguntaElegida, "<---------pregunta elegida")
        return preguntaElegida
    
    def obtenerPreguntas(self): return self.__preguntas
    
    
            
