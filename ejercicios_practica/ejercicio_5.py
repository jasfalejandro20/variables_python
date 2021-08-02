# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :

sub_text = palabra_1[0:3]
print('Las primeras tres letras de su palabra inicial serían:', sub_text)

# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados

sub_text1 = palabra_2[0:2]
print('Las primeras dos letras de su palabra final serían:', sub_text1)

# Imprima en pantalla los resultados
sub_text_max = sub_text + sub_text1
print('La combinación de las tres primeras y las dos últimas sería:', sub_text_max)