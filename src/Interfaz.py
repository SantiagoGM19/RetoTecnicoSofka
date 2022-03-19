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
        estaRegistrado = definirParticipante(ronda)
        while(estaRegistrado):
            print("Por favor intente nuevamente\n")
            estaRegistrado = definirParticipante(ronda)
        time.sleep(3)
        print()
        while(nivelRonda <= 5):
            pregunta = ronda.iniciarJuego()
            enunciado = pregunta[0]
            opciones = pregunta[1]
            opcionCorrecta = pregunta[2]
            categoria = pregunta[3]
            print("\nLa siguiente ronda trata sobre ",categoria, ":\n")
            time.sleep(2)
            mostrarPregunta(enunciado, opciones)
            esCorrecta = responder(ronda, opcionCorrecta)
            if(not esCorrecta or nivelRonda == 5): break
            nivelRonda = ronda.obtenerNivelDificultad()
                
    
    elif(opcion == "2"):
        print("Saliendo del juego")
        time.sleep(1)
        print("Hasta la próxima!")
    else:
        print("Por favor ingrese una opción válida")
        time.sleep(2)
        main()
        
def definirParticipante(ronda):
    nombre = input("Hola jugador, dinos tu nombre: ")
    nickName = input("Crea tu nickName para identificarte: ")
    estaRegistrado = ronda.definirJugador(nombre, nickName)
    return estaRegistrado

def mostrarPregunta(enunciado, opciones):
    print(enunciado)
    numOpcion = 1
    for opcion in opciones:
        print(str(numOpcion),".",opcion)
        numOpcion += 1
    print("5.Retirarse con el premio actual")
    
def responder(ronda, opcionCorrecta):
    try:
        respuesta = int(input("--->"))
        while(not(respuesta>=1 and respuesta<=5)):
            print("Tienes que elegir una de las cuatro opciones\n")
            respuesta = int(input("--->"))
        if(respuesta != 5):
            esCorrecta = ronda.responderPregunta(respuesta, opcionCorrecta)
            time.sleep(3)
        else:
            ronda.terminarRondaVoluntario()
            esCorrecta = False
        return esCorrecta
    except ValueError:
        print("\nEsa no es una opción válida, tiene que ser entre el 1 y 4."
              "Por favor intente de nuevo"
              )
        responder(ronda, opcionCorrecta)

        
main()
    