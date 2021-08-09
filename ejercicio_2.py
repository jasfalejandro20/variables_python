# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas

print('Bienvenido, analizaremos tus palabras, espero sea de tu agrado.')

texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

if texto_1 > texto_2:
    print ('{} es mayor que {}' .format(texto_1, texto_2))
else:
    print('{} es mayor que {}' .format(texto_2, texto_1))


# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

if len(texto_1) > len(texto_2):
    print('{} tiene mayor cantidad de letras que {}' .format(texto_1, texto_2))
else:
    print('{} tiene mayor cantidad de letras que {}' .format(texto_2, texto_1))

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

letra_inicial = texto_1[0] 
letra_inicial2 = texto_2[0]

if letra_inicial > letra_inicial2:
    print( 'La letra inicial {} de la primera palabra es mayor que la inicial {} de la segunda' .format(letra_inicial, letra_inicial2))
else:
    print('La letra inicial {} de la segunda palabra es mayor que la inicial {} de la segunda' .format(letra_inicial2, letra_inicial))


copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

if copia_texto_1 == texto_1:
    print(copia_texto_1)

print ('La palabra {} es igual a {}' .format(copia_texto_1,texto_1))

# Verifique que copia_texto_1 es distinta a texto_2

if copia_texto_1 != texto_2:
    print('La palabra {} es distinta a {}' .format(copia_texto_1, texto_2))

# Imprima en pantalla según corresponda