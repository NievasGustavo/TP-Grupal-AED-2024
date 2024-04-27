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


cp = input("Ingrese el código postal del lugar de destino: ")
direccion = input("Dirección del lugar de destino: ")
tipo = int(input("Tipo de envío (id entre 0 y 6 - ver tabla 2 en el enunciado): "))
pago = int(input("Forma de pago (1: efectivo - 2: tarjeta): "))


# 1. Indicar el nombre del país de destino basado en el formato de los CP de Argentina y
#    sus países vecinos. Si el CP no coincide con ninguno de estos formatos, se debe informar
#   que el país es "Otro".


# 2. Si el envío es dentro de Argentina, mostrar el nombre de la provincia de destino según
#    el estándar ISO 3166-2:AR. Si el envío es internacional o
#   hacia otro lugar fuera de Argentina, mostrar "No aplica".


# 3. Calcular el importe inicial a pagar por el envío, utilizando las tablas proporcionadas.
#    Si la forma de pago es en efectivo, aplicar un descuento del 10% al importe inicial
#   y mostrar por separado el importe final a pagar.


# 4. Mostrar los importes tanto inicial como final, incluso si son iguales.

"""
print("País de destino del envío:", destino)
print("Provincia destino:", provincia)
print("Importe inicial a pagar:", inicial)
print("Importe final a pagar:", final)
"""
