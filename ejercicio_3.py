# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Condicionales anidados
numero_1 = 7
numero_2 = -2

# Verifique si el numero_1 es mayor a 5

if numero_1 > 5:
    print(numero_1,'es mayor que 5')
else:
    print('5 es mayor que', numero_1)

#   --> En caso afirmativo, verifique si el numero_2
#       es positivo
#       --> En caso afirmativo imprima en pantalla "Resp=1"
#       --> En caso negativo imprima en pantalla   "Resp=2"
#  --> En caso negativo (numero_1 no es mayor a 5)
if numero_1 > 5 and numero_2 < 0:
    print ('Resp=2, es decir,', numero_2, 'es negativo')

#      verifique si el numero_2 es mayor a 5
#       --> En caso afirmativo imprima en pantalla "Resp=3"
#       --> En caso negativo imprima en pantalla "Resp=4"

if numero_2 > numero_1:
    print('Resp=4')

# Verifique la calificación de un estudiante según su
# puntaje en un examen

print ('Bienvenido, ingresa tu puntaje para saber tu calificación.')
puntaje = int(input())
# Si el puntaje es mayor igual a 90 --> imprimir A
if puntaje >= 90:
    print('Tu calificación es "A". ¡FELICIDADES!')

# Si el puntaje es mayor igual a 80 --> imprimir B
elif puntaje >= 80:
    print ('Tu calificación es "B". ¡GENIAL!')

# Si el puntaje es mayor igual a 70 --> imprimir C
elif puntaje >= 70:
    print('Tu calificación es "C". ¡VAMOS QUE PODRÁS CON TODO!')

# Si el puntaje es mayor igual a 60 --> imprimir D
elif puntaje >= 60:
    print('Tu calificación es "D". ¡VAMOS POR MÁS, ¡FELICIDADES!')
# Si el puntaje es menor a  60      --> imprimir F
elif puntaje < 60:
    print('Tu calificación es "F". No te desanimes, estamos aquí para ayudarte.')

# Debe imprimir en pantalla la calificacion
# Utilizar "if" anidados
