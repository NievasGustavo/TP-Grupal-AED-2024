import clase


def procesar_linea(linea):
    cp = linea[:9].strip()
    direc = linea[9:29].strip()
    tipo = linea[29].strip()
    fp = linea[30].strip()
    envio = clase.Envio(cp, direc, tipo, fp)
    return envio


def shellsort(envios):
    n = len(envios)
    gap = n // 2  # Inicialmente, el intervalo es la mitad de la longitud de la lista

    # Mientras el intervalo sea mayor que 0
    while gap > 0:
        # Realizamos un ordenamiento por inserción usando el intervalo actual
        for i in range(gap, n):
            temp = envios[i]
            j = i
            # Compara los elementos separados por el intervalo y los mueve si es necesario
            while j >= gap and envios[j - gap].codigo_postal > temp.codigo_postal:
                envios[j] = envios[j - gap]
                j -= gap
            envios[j] = temp

        # Reduce el intervalo
        gap //= 2

    return envios


def valid_direc(direc):
    last_car_mayus = False
    last_car_num = False
    pal_nums = False
    for car in direc:
        if car in " .":
            if pal_nums:
                return True
            last_car_mayus = False
        else:
            if car.isdigit() or car.isalpha():
                if last_car_mayus and car.isupper():
                    return False
                last_car_mayus = False
                if car.isupper():
                    last_car_mayus = True
                if car.isdigit() and last_car_num:
                    pal_nums = True
                else:
                    pal_nums = False
                if car.isdigit():
                    last_car_num = True
                else:
                    last_car_num = False
            else:
                return False


def procesar_archivo():
    v = []
    archivo = open("envios-tp3.txt", "r")
    control = archivo.readline()
    if "HC" in control or "hc" in control:
        tipo = "HC"
    else:
        tipo = "SC"
    for linea in archivo:
        envio = procesar_linea(linea)
        v.append(envio)
    archivo.close()
    v = shellsort(v)
    print(f"\n\033[92mSe cargaron {len(v)} envios\033[0m")
    return v, tipo


def mostrar_vector(v):
    cantidad = len(v)
    opcion = input(f"¿Desea mostrar los {cantidad} envios? (si: 0, no: 1) ")
    while not opcion.isnumeric() or int(opcion) < 0 or int(opcion) > 1:
        print("\n\033[91m ¤ ¡Opcion no valida! ¤ \033[0m\n")
        opcion = input("¿Desea mostrar todos los envios? (si: 0, no: 1) ")
    if int(opcion) == 0:
        for i in range(cantidad):
            print(f"{i + 1}) {v[i]}")
    else:
        nro_mostrar = input("Ingrese la cantidad de envios a mostrar: ")
        while not nro_mostrar.isnumeric() or int(nro_mostrar) < 0 or int(nro_mostrar) > len(v):
            print("\n\033[91m ¤ ¡Opcion no valida! ¤ \033[0m\n")
            nro_mostrar = input("Ingrese la cantidad de envios a mostrar: ")
        for i in range(int(nro_mostrar)):
            print(f"{i}) {v[i]}")


def menu():
    opciones = [
        "\n ╔════ Menu de opciones ════╗",
        "  1. Cargar por archivo",
        "  2. Carga manual",
        "  3. Mostrar todos los envíos",
        "  4. Buscar por dirección y tipo de envío",
        "  5. Buscar por código postal",
        "  6. Determinar cantidad de envíos",
        "  7. Determinar importe final de los envíos",
        "  8. Determinar envio con mayor importe final",
        "  9. Calcular promedio de importe por tipo de envío",
        "  0. Salir",
        "╚═══════════════════════════╝"
    ]

    for opcion in opciones:
        print(opcion)

    opcion_ingresada = input("Ingrese la opcion: ")

    if not opcion_ingresada.isnumeric() or int(opcion_ingresada) < 0 or int(opcion_ingresada) > 9:
        print("\n\033[91m ¤ ¡Opcion no valida! ¤ \033[0m\n")
        return menu()
    return int(opcion_ingresada)


def carga_manual(v):
    cp = input("Ingrese el código postal: ")
    direc = input("Ingrese la dirección de destino: ")

    tipo = input("Ingrese el tipo de envío: ")
    while not tipo.isnumeric() or int(tipo) < 0 or int(tipo) > 6:
        print("\n\033[91m ¤ ¡Opcion no valida! ¤ \033[0m\n")
        tipo = input("Ingrese el tipo de envío: ")

    fp = input("Ingrese la forma de pago: ")
    while not fp.isnumeric() or int(fp) < 0 or int(fp) > 1:
        print("\n\033[91m ¤ ¡Opcion no valida! ¤ \033[0m\n")
        fp = input("Ingrese la forma de pago: ")

    envio = clase. Envio(cp, direc, tipo, fp)
    v.append(envio)
    return v


def cant_envios(v, tipo):
    cant = [0] * 7
    if tipo == "HC":
        for envio in v:
            if valid_direc(envio.direccion):
                tipo_envio = int(envio.tipo)
                if 0 <= tipo_envio or tipo_envio <= 6:
                    cant[tipo_envio] += 1
    else:
        for envio in v:
            tipo_envio = int(envio.tipo)
            if 0 <= tipo_envio or tipo_envio <= 6:
                cant[tipo_envio] += 1

    for i in range(len(cant)):
        print(f"\n\033[92m Hay {cant[i]} envios de tipo {i}\033[0m")


def calc_imp(cp, env, pago, destino):
    # 3. Calcular el importe inicial del envío.
    inicial = 0
    final = 0
    if env == "0":
        inicial = 1100
    if env == "1":
        inicial = 1800
    if env == "2":
        inicial = 2450
    if env == "3":
        inicial = 8300
    if env == "4":
        inicial = 10900
    if env == "5":
        inicial = 14300
    if env == "6":
        inicial = 17900
    if destino != "Argentina":
        if destino in ("Bolivia", "Paraguay") or destino == "Uruguay" and int(cp[0]) == 1:
            inicial = int(inicial * 1.20)
        elif destino in ("Chile", "Uruguay"):
            inicial = int(inicial * 1.25)
        elif destino == "Brasil":
            if 0 <= int(cp[0]) <= 3:
                inicial = int(inicial * 1.25)
            elif 4 <= int(cp[0]) <= 7:
                inicial = int(inicial * 1.30)
            else:
                inicial = int(inicial * 1.20)
        else:
            inicial = int(inicial * 1.50)
        # Calculamos el pago final, aplicando el descuento
        #  del 10% al importe inicial si es en efectivo
    if pago == "1":
        final = int(inicial * 0.90)
    if pago == "2":
        final = inicial
    return final


def importe_final(v, tipo):
    cant = [0] * 7
    if tipo == "HC":
        for envio in v:
            if valid_direc(envio.direccion):
                tipo_envio = int(envio.tipo)
                if 0 <= tipo_envio or tipo_envio <= 6:
                    cant[tipo_envio] += calc_imp(envio.codigo_postal,
                                                 envio.tipo, envio.forma_pago, envio.pais)
    else:
        for envio in v:
            tipo_envio = int(envio.tipo)
            if 0 <= tipo_envio or tipo_envio <= 6:
                cant[tipo_envio] += calc_imp(envio.codigo_postal,
                                             envio.tipo, envio.forma_pago, envio.pais)

    for i in range(len(cant)):
        print("\n\033[92m El importe final de los envíos de tipo"
              f"{i} es de ${cant[i]}\033[0m")

    return cant


def may_importe(cant):
    primer_may = True
    for i in range(len(cant)):
        if primer_may:
            may = cant[i]
            primer_may = False
        else:
            if may < cant[i]:
                may = cant[i]
    print(f"\n\033[92m El mayor importe final es de ${may}\033[0m")

    return may


def porcentaje(cant, may_imp):
    total = 0
    for monto in cant:
        total += monto
    porcentaje_imp = int((may_imp / total) * 100)
    print(f"\n\033[92m El monto total mayor es de {porcentaje_imp}%"
          "sobre el monto total de envíos\033[0m")


def promedio_importe(cant):
    total = 0
    for monto in cant:
        total += monto
    prom = int(total / len(cant))
    print(f"\n\033[92m El promedio de importe final es de ${prom}\033[0m")

    return prom


def menor_importe(cant, imp_prom):
    cont_imp_men = 0
    for monto in cant:
        if imp_prom > monto:
            cont_imp_men += 1
    print(f"\n\033[92m El menor importe final es de ${cont_imp_men}\033[0m")


def buscar_tipo_direc(v, buscar_direccion, buscar_tipo_env):
    pass
