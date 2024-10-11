import os
import pickle
from clase import Envio

ARCHIVO_BINARIO = "envios.pydb"
ARCHIVO_CSV = "envios-tp4.csv"


def validador_numeros(num, minimo, maximo):
    while not num.isdigit() or int(num) < minimo or int(num) > maximo:
        num = input(f"Ingrese una opciòn entre {minimo} y {maximo}: ")
    return int(num)


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
    opciones = ["1. Carga por archivo", "2. Cargar manual", "3. Ver todos los envios",
                "4. Buscar por codigo postal", "5. Buscar por direccion",
                "6. Mostrar todas las combinaciones posibles",
                "7. Mostrar cantidad por tipo y fp", "8. Ver promedio de importe final", "0. Salir"]
    op = "-1"
    while not op.isnumeric() or int(op) < 0 or int(op) > 8:
        print("╔═════════════════════════════════════════════╗")
        print(f"║ {'Menu Principal':^43} ║")
        print("╠═════════════════════════════════════════════╣")
        for opcion in opciones:
            print(f"║ {opcion:<43} ║")
        print("╚═════════════════════════════════════════════╝")
        op = input("Ingrese una opcion: ")
        if op.isnumeric() and 0 <= int(op) <= 8:
            return int(op)
        mostrar_warning("Opcion invalida")


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
            cont += 1
        archivo_csv.close()
        archivo_binario.close()
        print(f"\n\033[92mSe cargaron los {cont-2} envios del archivo '{ARCHIVO_CSV}'\033[0m\n")
    else:
        mostrar_warning("No se encontro el archivo CSV")


def carga_manual():
    file = open(ARCHIVO_BINARIO, "ab")
    cp = input("Ingrese el Código Postal: ")
    while cp == "":
        cp = input("Ingrese un Código Postal valido: ")
    direc = input("Ingrese la Dirección: ")
    while direc == "":
        direc = input("Ingrese una Dirección valida: ")
    tipo = input("Ingrese el Tipo de envío: ")
    tipo = validador_numeros(tipo, 0, 6)
    forma_pago = input("Ingrese la Forma de Pago: ")
    forma_pago = validador_numeros(forma_pago, 1, 2)
    envio = Envio(cp, direc, tipo, forma_pago)
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
            print(f"\033[92m{envio}")
            cont += 1
        file.close()
        if cont > 1:
            print(f"Se muestran {cont} envios\033[0m\n")
        else:
            print(f"No hay envios en el archivo\033[0m\n")
    else:
        mostrar_warning("No se encontro el archivo binario")


def mostrar_envio_cp():
    if os.path.exists(ARCHIVO_BINARIO):
        cp = input("Ingrese el Código Postal: ")
        print()
        file = open(ARCHIVO_BINARIO, "rb")
        size = os.path.getsize(ARCHIVO_BINARIO)
        cont = 0
        while file.tell() < size:
            envio = pickle.load(file)
            if envio.codigo_postal == cp:
                print(f"\033[92m{envio}")
                cont += 1
        file.close()

        if cont == 1:
            print(f"\nSe muestra {cont} envio\033[0m\n")
        elif cont > 1:
            print(f"\nSe han mostrado {cont} envios\033[0m\n")
        else:
            print(f"\n\033[92mNo se encontro un envio con ese codigo postal\033[0m\n")
    else:
        mostrar_warning("No se encontro el archivo binario")


def mostrar_envio_dir():
    if os.path.exists(ARCHIVO_BINARIO):
        direc = input("Ingrese la Dirección termina con un .: ")
        file = open(ARCHIVO_BINARIO, "rb")
        size = os.path.getsize(ARCHIVO_BINARIO)
        while file.tell() < size:
            envio = pickle.load(file)
            if envio.direccion == direc:
                print(f"\033[92m{envio}\033[0m\n")
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
        for i in range(7):
            print(f"\033[92mTipo de envío {i}:")
            print(f"\tForma de pago 1: {cont[i][0]} envíos")
            print(f"\tForma de pago 2: {cont[i][1]} envíos")
            print()
        print("\033[0m")
        return cont
    mostrar_warning("No se encontro el archivo binario")


def contar_matriz(cont):
    total_por_tipo = [0] * 7
    total_por_fp = [0] * 2

    for i in range(7):
        for j in range(2):
            total_por_tipo[i] += cont[i][j]
            total_por_fp[j] += cont[i][j]

    print("\033[92mTotal por tipo de envío:")
    for i in range(7):
        print(f"\tTipo {i}: {total_por_tipo[i]} envíos")
    print()

    print("Total por forma de pago:")
    for i in range(2):
        print(f"\tForma de pago {i+1}: {total_por_fp[i]} envíos")
    print("\033[0m")


def shell_sort(v):
    n = len(v)
    ciclo = 1
    while ciclo <= n // 9:
        ciclo = 3 * ciclo + 1
    while ciclo > 0:
        for indx_actual in range(ciclo, n):
            envio = v[indx_actual]
            indx_temp = indx_actual - ciclo
            while indx_temp >= 0 and envio.codigo_postal < v[indx_temp].codigo_postal:
                v[indx_temp + ciclo] = v[indx_temp]
                indx_temp -= ciclo
            v[indx_temp + ciclo] = envio
        ciclo //= 3


def promedio_importes():
    if os.path.exists(ARCHIVO_BINARIO):
        file = open(ARCHIVO_BINARIO, "rb")
        size = os.path.getsize(ARCHIVO_BINARIO)
        total = 0
        cont = 0
        env_may = []
        while file.tell() < size:
            envio = pickle.load(file)
            cont += 1
            total += envio.importe
        if cont == 0:
            promedio = 0
        else:
            promedio = round(total / cont, 2)
        file.seek(0)
        while file.tell() < size:
            envio = pickle.load(file)
            if envio.importe > promedio:
                env_may.append(envio)
        shell_sort(env_may)
        file.close()
        for envio in env_may:
            print(f"\033[92m{envio}")
        print(f"Importe final promedio: {promedio}")
        print(f"Se mostraron {len(env_may)} envios\033[0m\n")
    else:
        mostrar_warning("No se encontro el archivo binario")


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
                    "Ingrese 1 para sobrescribirlo o cualquier otra tecla para continuar: ")
                if respuesta == "1":
                    cargar_archivo()
                continue
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
            # 7. En base a la matriz que se pidió generar en el ítem anterior
            if not cont:
                mostrar_warning(
                    "Debe ir por la opcion 6 antes de realizar esta accion")
            else:
                contar_matriz(cont)
        elif op == 8:
            promedio_importes()
        elif op == 0:
            print("\n\033[92mHasta pronto... 👀\033[0m\n")


if __name__ == "__main__":
    main()
