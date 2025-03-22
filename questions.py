import random
import sys
# Preguntas para el juego
questions = [
"¿Qué función se usa para obtener la longitud de una cadena en Python?",
"¿Cuál de las siguientes opciones es un número entero en Python?",
"¿Cómo se solicita entrada del usuario en Python?",
"¿Cuál de las siguientes expresiones es un comentario válido en Python?",
"¿Cuál es el operador de comparación para verificar si dos valores son iguales?",]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
("size()", "len()", "length()", "count()"),
("3.14", "'42'", "10", "True"),
("input()", "scan()", "read()", "ask()"),
(
"// Esto es un comentario",
"/* Esto es un comentario */",
"-- Esto es un comentario",
"# Esto es un comentario",
),
("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
puntaje_total = 0
# Se crea la lista con 3 tuplas, en la que cada una tiene su pregunta sus posibles respuestas y el indice de la respuesta valida
questions_to_ask = random.sample(list(zip(questions, answers, correct_answers_index)), k=3)
# Se crean las tuplas con las preguntas, respuestas e indices de las respuestas correctas en base a la variable questions_to_ask
for (preguntas, respuestas, indices) in (questions_to_ask):

# Se muestra la pregunta y las respuestas posibles
    print(preguntas)
    for i, answer in enumerate(respuestas):
        print(f"{i + 1}. {answer}")
# El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = (input("Respuesta: "))
# Verifico si es valida
        if user_answer.isdigit() and (0 < int(user_answer) <= len(answers[0])):
            user_answer = int(user_answer)-1
# Se verifica si la respuesta es correcta
            if user_answer == indices:
                print("¡Correcto!")
                puntaje_total += 1
                break
            else:
                puntaje_total -=0.5
        else:
            print("Respuesta no valida")
            sys.exit(1)
    else:
# Si el usuario no responde correctamente después de 2 intentos,
# se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(respuestas[indices])
# Se imprime un blanco al final de la pregunta
    print()
print(" el puntaje final fue: ",puntaje_total )