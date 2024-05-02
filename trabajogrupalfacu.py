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


cp = input("Ingrese el código postal del lugar de destino: ").upper()
"""
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (0: normal - 1: express - 2: "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))
"""

# 1. Indicar el nombre del país de destino basado en el formato de los CP de Argentina y
#    sus países vecinos. Si el CP no coincide con ninguno de estos formatos, se debe informar
#   que el país es "Otro".
if cp[0].isdigit():
    if cp.isdigit() and len(cp) == 4:
        destino = "Bolivia"
        provincia = "No aplica"

    elif len(cp[0:5]) == 5 and cp[5] == "-" and len(cp) == 9:
        destino = "Brasil"
        provincia = "No aplica"

    elif cp.isdigit() and len(cp) == 7:
        destino = "Chile"
        provincia = "No aplica"

    elif cp.isdigit() and len(cp) == 6:
        destino = "Paraguay"
        provincia = "No aplica"

    elif cp.isdigit() and len(cp) == 5:
        destino = "Uruguay"
        provincia = "No aplica"

    else:
        destino = "Otro"
        provincia = "No aplica"
# 2. Si el envío es dentro de Argentina, mostrar el nombre de la provincia de destino según
#    el estándar ISO 3166-2:AR. Si el envío es internacional o
#   hacia otro lugar fuera de Argentina, mostrar "No aplica".
else:
    if cp[0] != "I" or cp[0] != "O":
        destino = "Argentina"
        if cp[0] == "A":
            provincia = "Salta"
        if cp[0] == "B":
            provincia = "Buenos Aires"
        if cp[0] == "C":
            provincia = "CABA"
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
        if cp[0] == "J":
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
            provincia = "Neuquén"
        if cp[0] == "R":
            provincia = "Rio Negro"
        if cp[0] == "S":
            provincia = "Santa Fe"
        if cp[0] == "T":
            provincia = "Tucumano"
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
    else:
        destino = "Otro"
        provincia = "No aplica"
# 3. Calcular el importe inicial a pagar por el envío, utilizando las tablas proporcionadas.
#    Si la forma de pago es en efectivo, aplicar un descuento del 10% al importe inicial
#   y mostrar por separado el importe final a pagar.


# 4. Mostrar los importes tanto inicial como final, incluso si son iguales.


print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
"""
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)
"""
