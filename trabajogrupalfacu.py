"""
El programa debe permitir al usuario ingresar los siguientes datos del envío:
    ● código postal (CP) del destino
    ● dirección física del destino tipo de envío (un número entre 0 y 6)
    ● forma de pago (1 para efectivo, 2 para tarjeta de crédito).

Después de ingresar los datos del envío, el programa debe realizar lo siguiente:

    1. Indicar el nombre del país de destino basado en el formato de los CP de Argentina y
    sus países vecinos. Si el CP no coincide con ninguno de estos formatos, se debe informar
    que el país es "Otro".

    2. Si el envío es dentro de Argentina, mostrar el nombre de la provincia de destino según
    el estándar ISO 3166-2:AR. Si el envío es internacional o
    hacia otro lugar fuera de Argentina, mostrar "No aplica".

    3. Calcular el importe inicial a pagar por el envío, utilizando las tablas proporcionadas.
    Si la forma de pago es en efectivo, aplicar un descuento del 10% al importe inicial
    y mostrar por separado el importe final a pagar.

    4. Mostrar los importes tanto inicial como final, incluso si son iguales.

Datos:
    ● La dirección física del destino: una cadena de caracteres (sin validación ni formato especial
    requerido) indicando la dirección concreta de entrega.

    ● El tipo de envío: un número entero entre 0 y 6 que indica alguno de los siete tipos posibles
    (ver columna "Id" en la tabla de tipos de envío - Tabla 2). Se asume que el usuario cargará
    estrictamente alguno de esos dígitos, y ningún otro.

    ● La forma de pago: un número entero que indica alguno de los dos siguientes tipos de pago:
    (1: efectivo, 2: tarjeta de crédito). Se asume que el usuario cargará estrictamente alguno de
    esos dígitos, y ningún otro.
"""


# El programa debe permitir al usuario ingresar los siguientes datos del envío:
#   ● código postal (CP) del destino
#   ● dirección física del destino
#   ● tipo de envío (un número entre 0 y 6)
#   ● forma de pago (1 para efectivo, 2 para tarjeta de crédito).


cp = input("Ingrese el código postal del lugar de destino:")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 ): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))

##PAISES:
long =len(cp)
if long == 8:
 destino = "Argentina"
if cp[0] == "A":
    provincia = "Salta"
if cp[0] == "B":
    provincia = "Provincia de Buenos Aires"
if cp[0] == "C":
    provincia = "Ciudad Autónoma de Buenos Aires"
if cp[0] == "D":
    provincia = "San Luis"
if cp[0] == "E":
    provincia = "Entre Ríos"
if cp[0] == "F":
    provincia = "La Rioja"
if cp[0] == "G":
    provincia = "Santiago del Estero"
if cp[0] == "H":
    provincia = "Chaco"
if cp[0] == "J  ":
    provincia = "San Juan"
if cp[0] == "K":
    provincia = "Catamarca"
if cp[0] == "L":
    provincia = "La Pampa"
if cp[0] == "M":
    provincia = "Mendoza"
if cp[0] == "N":
    provincia = "Misiones"
if cp[0] == "P":
    provincia = "Formosa"
if cp[0] == "Q":
    provincia = "Nequen"
if cp[0] == "R":
    provincia = "Rio Negro"
if cp[0] == "S":
    provincia = "Santa Fe"
if cp[0] == "T":
    provincia = "Tucuman"
if cp[0] == "U":
    provincia = "Chubut"
if cp[0] == "V":
    provincia = "Tierra del Fuego"
if cp[0] == "W":
    provincia = "Corrientes"
if cp[0] == "X":
    provincia = "Cordoba"
if cp[0] == "Y":
    provincia = "Jujuy"
if cp[0] == "Z":
    provincia = "Santa Cruz"
if cp[0] == "I" or cp[0] == "Ñ" or cp[0] == "O":
    provincia = "No Aplica"


if long == 4:
  destino = "Bolivia"
  provincia = "No Aplica"
if long == 9:
  destino = "Brasil"
  provincia = "No Aplica"
if long == 7:
  destino = "Chile"
  provincia = "No Aplica"
if long == 6:
 destino = "Paraguay"
 provincia = "No Aplica"
if long == 5:
 destino = "Uruguay"
 provincia = "No Aplica"
if long <=3 or long >=10:
    destino = "Otros Paises"
    provincia = "No Aplica"



#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#PRECIO POR PESO:
if tipo == 0:
   inicial = 1100
if tipo == 1:
   inicial = 1800
if tipo == 2:
   inicial = 2450
if tipo == 3:
   inicial = 8300
if tipo == 4:
   inicial = 10900
if tipo == 5:
   inicial = 14300
if tipo == 6:
   inicial = 17900

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#ENVIOS INTERNACIONALES:
if destino == "Uruguay" and cp[0] == 1:
    porcentaje = (inicial * 20) /100
    inicial = inicial + porcentaje
else:
    porcentaje = (inicial * 25) / 100
    inicial = inicial + porcentaje

if destino == "Bolivia" or destino == "Paraguay":
    porcentaje = (inicial * 20) / 100
    inicial = inicial + porcentaje

if destino == "Chile":
    porcentaje = (inicial * 25) / 100
    inicial = inicial + porcentaje

if direccion == "Brasil" and cp[0] >= 8 :
    porcentaje = (inicial * 20) / 100
    inicial = inicial + porcentaje
if direccion == "Brasil" and cp[0] >= 0 and cp[0] <= 3:
    porcentaje = (inicial * 25) / 100
    inicial = inicial + porcentaje
if direccion == "Brasil" and cp[0] >= 4 and cp[0] <= 7:
    porcentaje = (inicial * 30) / 100
    inicial = inicial + porcentaje

if destino == "Otros Paises":
    porcentaje = (inicial * 50) / 100
    inicial = inicial + porcentaje

if pago == 1:
    final = inicial - ((inicial * 10) / 100)
else:
    final = inicial
print()
print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)
