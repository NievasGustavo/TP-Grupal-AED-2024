import os
import pickle
from clase import Envio
import helpers


ARCHIVO_BINARIO = "envios.pydb"
ARCHIVO_CSV = "envios-tp4.csv"


def menu():
    opciones = ["╔═══════════════════════════╗",
                "║       Menu Principal      ║",
                "╠═══════════════════════════╣ ",
                "║ 1. Crear archivo          ║ ",
                "║ 2. Cargar manual          ║ ",
                "║ 3. Ver envios             ║ ",
                "║ 4. ver por codigo postal  ║ ",
                "║ 5. ver por direccion      ║ ",
                "║ 6. Cargar archivo         ║ ",
                "║ 7. Cargar archivo         ║ ",
                "║ 8. Cargar archivo         ║ ",
                "║ 0. Salir                  ║ ",
                "╚═══════════════════════════╝"]
    for opcion in opciones:
        print(opcion)

    op = input("Ingrese una opcion: ")
    while not op.isnumeric() or int(op) < 0 or int(op) > 8:
        print("\n\033[91m ¡Ingrese una opción valida! \033[0m\n")
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
        print("\n\033[91mEl archivo csv no existe\033[0m\n")


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
        print("\n\033[91mNo hay envios\033[0m\n")


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
        print("\n\033[91mNo hay envios\033[0m\n")


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
        print("\n\033[91m╔═══════════════════════════╗\033[0m")
        print("\033[91m║ No se encontro el envío   ║\033[0m")
        print("\033[91m╚═══════════════════════════╝\033[0m")
        file.close()
        print()
    else:
        print("\n\033[91mNo hay envios\033[0m\n")


def calcular_envios():
    if os.path.exists(ARCHIVO_BINARIO):
        file = open(ARCHIVO_BINARIO, "rb")
        size = os.path.getsize(ARCHIVO_BINARIO)
        cont = [[0] * 2 for i in range(7)]
        while file.tell() < size:
            envio = pickle.load(file)
            cont[int(envio.tipo) - 1][int(envio.forma_pago) - 1] += 1
        file.close()
        for i in range(7):
            for j in range(2):
                if cont[i][j] > 0:
                    print(
                        f'\033[92mTipo de envío {i}, Forma de pago {j}: {cont[i][j]} envíos\033[0m')
        print()
        return cont
    else:
        print("\n\033[91mNo hay envios\033[0m\n")


def main():
    op = -1
    v = []
    while op != 0:
        op = menu()
        if op == 1:
            if os.path.exists(ARCHIVO_BINARIO):
                print("\n\033[91m╔═══════════════════════════╗\033[0m")
                print(
                    "\033[91m║ El archivo ya existe.     ║\n║ ¿Desea sobrescribirlo?    ║\033[0m")
                print("\033[91m╚═══════════════════════════╝\033[0m")
                respuesta = input(
                    "Ingrese 1 para sobrescribirlo o cualquier otra tecla para continuar: ")
                if respuesta == "1":
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
            calcular_envios()
        elif op == 7:
            print("\n\033[91mFuncionalidad no disponible\033[0m\n")
        elif op == 8:
            print("\n\033[91mFuncionalidad no disponible\033[0m\n")
        elif op == 0:
            print("\n\033[92mSaliendo...\033[0m\n")


if __name__ == "__main__":
    main()
