import os
import pickle
from clase import Envio
import helpers


ARCHIVO_BINARIO = "envios.pydb"
ARCHIVO_CSV = "envios-tp4.csv"


def mostrar_warning(mensaje):
    max_car = 43

    if len(mensaje) > max_car:
        palabras = mensaje.split()
        renglones = []
        renglon_actual = ""

        for palabra in palabras:
            if len(renglon_actual) + len(palabra) + 1 <= max_car:
                renglon_actual += (palabra + " ")
            else:
                renglones.append(renglon_actual.rstrip())
                renglon_actual = palabra + " "
        renglones.append(renglon_actual.rstrip())

    else:
        renglones = [mensaje]

    print("\n\033[91m╔═════════════════════════════════════════════╗")
    for renglon in renglones:
        print(f"║ {renglon:<43} ║")
    print("╚═════════════════════════════════════════════╝\033[0m")


def menu():
    opciones = ["╔═════════════════════════════════════════════╗",
                "║               Menu Principal                ║",
                "╠═════════════════════════════════════════════╣ ",
                "║ 1. Crear archivo                            ║ ",
                "║ 2. Cargar manual                            ║ ",
                "║ 3. Ver envios                               ║ ",
                "║ 4. Ver por codigo postal                    ║ ",
                "║ 5. Ver por direccion                        ║ ",
                "║ 6. Mostrar todas las combinaciones posibles ║ ",
                "║ 7. Mostrar por tipo de envío y forma de pago║ ",
                "║ 8. Cargar archivo                           ║ ",
                "║ 0. Salir                                    ║ ",
                "╚═════════════════════════════════════════════╝"]
    for opcion in opciones:
        print(opcion)

    op = input("Ingrese una opcion: ")
    while not op.isnumeric() or int(op) < 0 or int(op) > 8:
        mostrar_warning("Opcion no valida")
        for opcion in opciones:
            print(opcion)
        op = input("Ingrese una opcion: ")
    return int(op)


def cargar_archivo():
    if os.path.exists(ARCHIVO_CSV):
        archivo_csv = open(ARCHIVO_CSV, "rt")
        archivo_binario = open(ARCHIVO_BINARIO, "wb")
        cont = 0
        for linea in archivo_csv:
            if cont < 2:
                cont += 1
                continue
            linea = linea.strip().split(",")
            envio = Envio(linea[0], linea[1], linea[2], linea[3])
            pickle.dump(envio, archivo_binario)
        archivo_csv.close()
        archivo_binario.close()
        print("\n\033[92mSe cargo el archivo\033[0m\n")
    else:
        mostrar_warning("No se encontro el archivo CSV")


def carga_manual():
    file = open(ARCHIVO_BINARIO, "ab")
    cp = input("Ingrese el Código Postal: ")
    while cp == "":
        cp = input("Ingrese un Código Postal valido: ")
    dir = input("Ingrese la Dirección: ")
    while dir == "":
        dir = input("Ingrese una Dirección valida: ")
    tipo = input("Ingrese el Tipo de envío: ")
    helpers.validador_numeros(tipo, 1, 3)
    fp = input("Ingrese la Forma de Pago (1. Efectivo, 2. Tarjeta): ")
    helpers.validador_numeros(fp, 1, 2)
    envio = Envio(cp, dir, tipo, fp)
    pickle.dump(envio, file)
    file.close()
    print("\n\033[92mSe cargo el envío\033[0m\n")


def ver_envios():
    if os.path.exists(ARCHIVO_BINARIO):
        file = open(ARCHIVO_BINARIO, "rb")
        size = os.path.getsize(ARCHIVO_BINARIO)
        cont = 0
        while file.tell() < size:
            envio = pickle.load(file)
            print(envio)
            cont += 1
        file.close()
        print(f"\n\033[92mSe muestran {cont} envios\033[0m\n")
    else:
        mostrar_warning("No se encontro el archivo binario")


def mostrar_envio_cp():
    if os.path.exists(ARCHIVO_BINARIO):
        cp = input("Ingrese el Código Postal: ")
        file = open(ARCHIVO_BINARIO, "rb")
        size = os.path.getsize(ARCHIVO_BINARIO)
        cont = 0
        while file.tell() < size:
            envio = pickle.load(file)
            if envio.codigo_postal == cp:
                print(envio)
                cont += 1
        file.close()
        print(f"\n\033[92mSe han mostrado {cont} envios\033[0m\n")
    else:
        mostrar_warning("No se encontro el archivo binario")


def mostrar_envio_dir():
    if os.path.exists(ARCHIVO_BINARIO):
        direc = input("Ingrese la Dirección: ")
        file = open(ARCHIVO_BINARIO, "rb")
        size = os.path.getsize(ARCHIVO_BINARIO)
        while file.tell() < size:
            envio = pickle.load(file)
            if envio.direccion == direc:
                print(f"\033[92m{envio}'\033[0m\n")
                file.close()
                return
        mostrar_warning("No se encontro el envío")
        file.close()
        print()
    else:
        mostrar_warning("No se encontro el archivo binario")


def calcular_envios():
    if os.path.exists(ARCHIVO_BINARIO):
        file = open(ARCHIVO_BINARIO, "rb")
        size = os.path.getsize(ARCHIVO_BINARIO)
        cont = [[0] * 2 for i in range(7)]
        while file.tell() < size:
            envio = pickle.load(file)
            cont[int(envio.tipo) - 1][int(envio.forma_pago) - 1] += 1
        file.close()
        print(cont)
        for i in range(7):
            for j in range(2):
                if cont[i][j] > 0:
                    print(
                        f'\033[92mTipo de envío {i}, Forma de pago {j+1}: {cont[i] [j]} envíos\033[0m')
        print()
        return cont
    else:
        print("\n\033[91m╔═════════════════════════════════════════════╗")
        print("║ No se encontro el archivo binario.          ║")
        print("╚═════════════════════════════════════════════╝\033[0m")


def contar_matriz(cont):
    total_por_tipo = [0] * 7
    total_por_pago = [0] * 2

    for i in range(7):
        for j in range(2):
            total_por_tipo[i] += cont[i][j]
            total_por_pago[j] += cont[i][j]

    print("\033[92mTotal por tipo de envío:")
    for i in range(7):
        print(f"\tTipo {i}: {total_por_tipo[i]} envíos")
    print()

    print("Total por forma de pago:")
    for i in range(2):
        print(f"\tForma de pago {i+1}: {total_por_pago[i]} envíos")
    print("\033[0m")


def main():
    op = -1
    cont = []
    while op != 0:
        op = menu()
        if op == 1:
            if os.path.exists(ARCHIVO_BINARIO):
                mostrar_warning(
                    "Ya existe un archivo binario. ¿Desea sobrescribirlo?")
                respuesta = input(
                    "Ingrese y para sobrescribirlo o cualquier otra tecla para continuar: ")
                if respuesta == "y":
                    cargar_archivo()
            else:
                cargar_archivo()

        elif op == 2:
            carga_manual()
        elif op == 3:
            ver_envios()
        elif op == 4:
            mostrar_envio_cp()
        elif op == 5:
            mostrar_envio_dir()
        elif op == 6:
            cont = calcular_envios()
        elif op == 7:
            if not cont:
                print("\n\033[91mDebe ir por la opcion 6\033[0m\n")
            else:
                contar_matriz(cont)
        elif op == 8:
            print("\n\033[91mFuncionalidad no disponible\033[0m\n")
        elif op == 0:
            print("\n\033[92mSaliendo...\033[0m\n")


if __name__ == "__main__":
    main()
