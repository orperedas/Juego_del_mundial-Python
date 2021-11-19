"""
Este es un ejercicio para saber cuán fanático sos de la Selección Argentina.

En primer lugar, tiene dos funciones que se encargan de hacer el trabajo, es decir, donde está toda la lógica del programa: evaluar_respuesta() y cuestionario() que se explican con mayor amplitud más adelante.
"""

# list_preguntas() tiene en su interior una lista con las preguntas a responder, cuyos valores se encuentran separados por líneas para leerlos fácilmente y que retorna como valor la lista completa para que sea usada en las otras funciones.
def list_preguntas():
    list_p = [
        "¿Cuántos mundiales de fútbol ha ganado Argentina?",
        "¿Quién es el máximo goleador de la selección Argentina?",
        "¿Cuántos goles anotó El Diego en el mundial del 86?",
        "¿En qué año ganó Argentina su primer mundial de fútbol",
        "¿Quién era el portero de Argenina en México 86?"
    ]
    return list_p

# list_respuestas() tiene en su interior una lista con las respuestas correctas, cuyos valores se encuentran separados por líneas para leerlos fácilmente y que retorna como valor la lista completa para que sea usada en las otras funciones.


def list_respuestas():
    list_r = [
        2,
        "Lionel Messi",
        5,
        1978,
        "Nery Punpido"
    ]
    return list_r

# dict_opciones() tiene en su interior un diccionario anidado, cuyas claves y valores son las opciones de respuestas que el usuario puede elegir para cada pregunta, se encuentran separados por líneas para leerlos fácilmente; esta función retorna como valor el diccionario completo para que sea usada en las otras funciones.
def dict_opciones():
    dict_o = {
        1: {
            "A": 3,
            "B": 1,
            "C": 2
        },
        2: {
            "A": "Gabriel Batistuta",
            "B": "Lionel Messi",
            "C": "Diego Maradona"
        },
        3: {
            "A": 6,
            "B": 5,
            "C": 7
        },
        4: {
            "A": 1930,
            "B": 1978,
            "C": 1986
        },
        5: {
            "A": "Nery Punpido",
            "B": "Sergio Goicoechea",
            "C": "Ubaldo Fillol"
        }
    }
    return dict_o

# evaluar_respuesta() esta función se encarga de evaluar según el argumento "indice_pregunta" si la opción de respuesta ingresada por el usuario es correcta, si lo es le suma 1 al valor de la variable puntaje; por último, retorna el puntaje obtenido luego de haber respondido todo el cuestionario.
def evaluar_respuesta(indice_pregunta):
    respuestas = list_respuestas() # Asignación de la lista de respuestas que retorna la función list_respuestas.
    opciones = dict_opciones() # Asignación del diccionario de opciones que retorna la función dict_opciones.
    puntaje = 0
    opcion_ingresada = (input("ingrese su opcion: ").upper()) # solicita al usuario ingresar la letra de la opción de la respuesta ejegida y la convierte a mayúscula

    # Condicional que evalúa si debe sumar el valor de uno a la variable puntaje si la respuesta ingresada por el usuario es correcta.
    if opciones[indice_pregunta + 1][opcion_ingresada] == respuestas[indice_pregunta]:
        puntaje += 1
        print(f"tu puntaje en esta pregunta es: {puntaje}")
    else:
        print("No tienes puntos en esta respuesta.")

    # Retorno del puntaje obtenido por el usuario.
    return puntaje

# cuestionario() esta función se encarga de dar la bienvenida al usuario y darle las instrucciones del cuestionario, luego muestra la primera pregunta y las opciones de respuesta para que el ususario elija una opción, el proceso se repite con cada una de las preguntas; por último devuelve un mensaje específico según el puntaje obtenido.
def cuestionario():
    preguntas = list_preguntas() # Asignación de la lista de preguntas que retorna la función list_preguntas. 
    opciones = dict_opciones()# Asignación del diccionario de opciones que retorna la función dict_opciones.
    total_preguntas = len(preguntas) # Longitud de total de los valores de la lista preguntas.
    indice_pregunta = preguntas.index(preguntas[0]) +1 # variable que devuelve un número de índice de la lista preguntas
    puntaje_total = 0 # Asignación del valor 0, como inicial de la variable.

    # Mensaje de vienvenida e instrucciones del programa.
    print("\nHola, bienbenido al cuestionario para fanáticos de la Selección Argentina.\nSi sos un conocedor de la historia de la Selección seguro responderás este cuestionario con los ojos cerrados.")
    print("\nInstrucciones:\nRecibirás una serie de preguntas sobre la historia de la Selección Argentina, cada pregunta tiene una serie de opciones para elegir como respuesta correcta.\ningresa la letra de la opción que consideres correcta y presiona ENTER para registrar tu respuesta.")

    # Recorre la lista de preguntas y las imprime según el número que muestra el iterador.
    for indice_pregunta in range(total_preguntas):
        print(indice_pregunta+1, "-", preguntas[indice_pregunta])

        # Rocorre el diccionario anidado opciones, por los items anidados según el número de pregunta del iterador de bucle anterior e imprime las opciones.
        for opciones_respuesta in opciones[indice_pregunta + 1].items():
            print(f"     {opciones_respuesta[0]} - {opciones_respuesta[1]}")

        puntaje_total += evaluar_respuesta(indice_pregunta) # Asignación del valor de retorno de la función evaluar_respuesta.
        print(f"El puntaje total es: {puntaje_total}") # Imprime mensaje que incluye el puntaje obtenido

    # Condicional que devuelve un mensaje específico según el puntaje_total.
    if puntaje_total == len(opciones):
        print("¡Sos GRANDE, vos sí sos un Argentino de verdad!")
    elif puntaje_total == len(opciones)-1:
        print(f"¡Muy bien, tenés {puntaje_total} buenas, sabés bastate de la hitoria de la sección, pero podés mejorar!")
    elif puntaje_total == len(opciones)-2:
        print(f"{puntaje_total} de {len(opciones)} no está mal, pero...")
    elif puntaje_total == len(opciones)-3:
        print(f"¿Solo {puntaje_total} respuestas correctas, qué, vos ?")
    elif puntaje_total == len(opciones)-4:
        print(f"¡No, no, no, ¿{puntaje_total} respuesta correcta?, ¡qué vergüenza, che!")
    else:
        print("Vos tenés que volver a la escuela, no sabés nada de la selección!")

cuestionario()
