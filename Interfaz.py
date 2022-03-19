import time
from Ronda import *

print("¡Bienvenido al Concurso de preguntas! \n")
def main():
    print("1. Comenzar juego")
    print("2. Salir \n")
    
    opcion = input("Ingrese una opción por favor para ejecutar o salir: ")
    
    if(opcion == "1"):
        ronda = Ronda()
        nivelRonda = ronda.obtenerNivelDificultad()
        while(nivelRonda <= 5):
            pregunta = ronda.iniciarJuego()
            enunciado = pregunta[0]
            opciones = pregunta[1]
            opcionCorrecta = pregunta[2]
            categoria = pregunta[3]
            print("\nLa siguiente ronda trata sobre ",categoria, ":\n")
            mostrarPregunta(enunciado, opciones)
            responder(ronda, opcionCorrecta)
                
    
    elif(opcion == "2"):
        print("Saliendo del juego")
        time.sleep(1)
        print("Hasta la próxima!")
    else:
        print("Por favor ingrese una opción válida")
        time.sleep(2)
        main()

def mostrarPregunta(enunciado, opciones):
    print(enunciado)
    numOpcion = 1
    for opcion in opciones:
        print(numOpcion, ".", opcion)
        numOpcion += 1
    
def responder(ronda, opcionCorrecta):
    respuesta = int(input())
    while(not(respuesta>=1 and respuesta<=4)):
        print("Tienes que elegir una de las cuatro opciones\n")
        respuesta = int(input())
    ronda.responderPregunta(respuesta, opcionCorrecta)
        

        
main()
    