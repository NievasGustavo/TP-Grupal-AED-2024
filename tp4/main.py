from clase import Envio
import os
import pickle
import helpers

def menu():
    opciones = ["╔═══════════════════════════╗",
                "║       Menu Principal      ║",
                "╠═══════════════════════════╣ ",
                "║ 1. Crear archivo          ║ ",
                "║ 2. Cargar manual          ║ ",
                "║ 3. Ver envios             ║ ",
                "║ 4. Cargar archivo         ║ ",
                "║ 5. Guardar archivo        ║ ",
                "║ 6. Cargar archivo         ║ ",
                "║ 7. Cargar archivo         ║ ",
                "║ 8. Cargar archivo         ║ ",
                "║ 0. Salir                  ║ ",
                "╚═══════════════════════════╝"]

    while True:
        for opcion in opciones:
            print(opcion)
        op = input("Ingrese una opcion: ")
        if op.isnumeric() and 0 <= int(op) <= 4:
            return int(op)
        print("\n\033[91m ¡Ingrese una opcion valida! \033[0m\n")


def cargar_archivo():
    if os.path.exists("envios-tp4.csv"):
        file = open("envios-tp4.csv", "rt")
        file.readline()
        file.readline()
        archivo = open("envios.dat", "wb")
        for line in file:
            line = line.strip().split(",")
            envio = Envio(line[0], line[1], line[2], line[3])
            pickle.dump(envio, archivo)
        file.close()
        archivo.close()
        print("\n\033[92mSe cargaron los envios\033[0m\n")


def carga_manual():
    if os.path.exists("envios.dat"):
        file = open("envios.dat", "ab")
    else:
        file = open("envios.dat", "wb")
    cp = input("Ingrese el Código Postal: ")
    dir = input("Ingrese la Dirección: ")
    tipo = input("Ingrese el Tipo de envío (1. Retiro en sucursal, 2. Envío a domicilio, 3. Envío a persona): ")
    helpers.validador_numeros(tipo, 1, 3)
    fp = input("Ingrese la Forma de Pago (1. Efectivo, 2. Tarjeta): ")
    helpers.validador_numeros(fp, 1, 2)
    envio = Envio(cp, dir, tipo, fp)
    pickle.dump(envio, file)
    file.close()
    print("\n\033[92mSe cargo el envío\033[0m\n")

def ver_envios():
    if os.path.exists("envios.dat"):
        file = open("envios.dat", "rb")
        size = os.path.getsize("envios.dat")
        while file.tell() < size:
            envio = pickle.load(file)
            print(envio)
        file.close()
    else:
        print("\n\033[91mNo hay envios\033[0m\n")


def main():
    op = -1
    while op != 0:
        op = menu()
        if op == 1:
            if os.path.exists("envios.dat"):
                print("\n\033[91mEl archivo ya existe. ¿Desea sobrescribirlo?\033[0m\n")
                respuesta = input("Ingrese 1 para sobrescribirlo o 0 para cancelar: ")
                if respuesta == "1":
                    cargar_archivo()
            else:
                cargar_archivo()

        elif op == 2:
            carga_manual()
        elif op == 3:
            ver_envios()


if __name__ == "__main__":
    main()
