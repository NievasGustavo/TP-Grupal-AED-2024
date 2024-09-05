import clase


def procesar_linea(linea):
    cp = linea[:9].strip()
    direc = linea[9:29].strip()
    tipo = linea[29].strip()
    fp = linea[30].strip()
    envio = clase.Envio(cp, direc, tipo, fp)
    return envio


def selection_sort(envios, parametro='cp'):
    """
    Ordena un vector de envios segun el parametro seleccionado

    Parametro envios: Vector de envios a ordenar
    Parametro parametro: Parametro segun el cual se ordena el vector
        'cp': Ordena por codigo postal
        'direccion': Ordena por direccion
        'tipo': Ordena por tipo de envio

    Retorna el vector de envios ordenado
    """
    n = len(envios)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if parametro == 'direccion':
                if envios[j].direccion < envios[min_idx].direccion:
                    min_idx = j
            elif parametro == 'tipo':
                if envios[j].tipo < envios[min_idx].tipo:
                    min_idx = j
            elif parametro == 'cp':
                if envios[j].codigo_postal < envios[min_idx].codigo_postal:
                    min_idx = j
        envios[i], envios[min_idx] = envios[min_idx], envios[i]
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
    v = selection_sort(v)
    print(f"\n\033[92mSe cargaron {len(v)} envios\033[0m")
    return v, tipo


def mostrar_vector(v):
    """
    Muestra todos los envios en el vector o una cantidad determinada por el usuario

    Parametro v: Vector de envios
    """
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
        "  5. Buscar por código postal y cambiar de forma de pago",
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
        input("Ingrese cualquier tecla para continuar...")
        return menu()
    return int(opcion_ingresada)


def carga_manual(v):
    """
    Funcion que carga un envío manualmente.
    Crea un objeto Envío con los datos ingresados y lo agrega al vector.
    Luego muestra el envío cargado y retorna el vector actualizado.

    Parametro v: Vector de envios
    Retorna: Vector actualizado
    """

    cp = input("Ingrese el código postal: ")
    direc = input("Ingrese la dirección de destino: ")

    tipo = input("Ingrese el tipo de envío: ")
    while not tipo.isnumeric() or int(tipo) < 0 or int(tipo) > 6:
        print("\n\033[91m ¤ ¡Tipo de envío no valido! ¤ \033[0m\n")
        tipo = input("Ingrese el tipo de envío: ")

    fp = input("Ingrese la forma de pago: ")
    while not fp.isnumeric() or int(fp) < 0 or int(fp) > 1:
        print("\n\033[91m ¤ ¡Forma de pago no valida! ¤ \033[0m\n")
        fp = input("Ingrese la forma de pago: ")

    envio = clase. Envio(cp, direc, tipo, fp)
    v.append(envio)

    print(f"\n\033[92mSe cargo el envío {envio}\033[0m")
    return v


def cant_envios(v, tipo):
    """
    Funcion que devuelve un vector con la cantidad de envíos de cada tipo en el vector de envíos

    Parametro v: Vector de envíos
    Parametro tipo: Tipo de control de envíos, puede ser "HC" o "SC"
    Retorna un vector con la cantidad de envíos de cada tipo
    """
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
    """
    Funcion que devuelve un vector con el importe final de cada tipo de envío
    en el vector de envíos.

    Parametro v: Vector de envíos
    Parametro tipo: Tipo de control de envíos, puede ser "HC" o "SC"
    Retorna un vector con el importe final de cada tipo de envío
    """
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
        print("\n\033[92m El importe final de los envíos de tipo "
              f"{i} es de ${cant[i]}\033[0m")

    return cant


def may_importe(cant):
    """
    Funcion que determina el mayor importe final en el vector de cantidades
    y lo imprime.

    Parametro cant: Vector con las cantidades de cada tipo de envío
    Retorna el mayor importe final
    """
    primer_may = True
    for i in range(len(cant)):
        if primer_may:
            may = i
            primer_may = False
        else:
            if cant[may] < cant[i]:
                may = i
    print(f"\n\033[92m El mayor importe final es de ${cant[may]} que pertenece al envío de tipo {may}\033[0m")

    return may


def porcentaje(cant, may_imp):
    total = 0
    for monto in cant:
        total += monto
    porcentaje_imp = int((cant[may_imp] / total) * 100)
    print(f"\n\033[92m El mayor importe final representa {porcentaje_imp}% del total de envíos\033[0m")


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
    print(f"\n\033[92m La cantidad de envíos menores al promedio es de {cont_imp_men}\033[0m")


def busqueda_lineal(v, primer_parametro, segundo_parametro=None):
    for envio in v:
        if segundo_parametro is not None:
            if envio.direccion == primer_parametro and envio.tipo == segundo_parametro:
                print(f"\n\033[92m El envío encontrado es: {envio}\033[0m")
                return envio
        elif envio.codigo_postal == primer_parametro:
            print(f"\n\033[92m El envío encontrado es: {envio}\033[0m")
            return envio
    print("\n\033[91m ¡No se ha encontrado el envío!\033[0m")


def busqueda_binaria(v, primer_parametro, segundo_parametro=None):
    izq, der = 0, len(v) - 1
    while izq <= der:
        med = (izq + der) // 2
        pivote = v[med]

        if segundo_parametro is not None:
            if pivote.direccion == primer_parametro and pivote.tipo == segundo_parametro:
                print(f"\n\033[92m El envío encontrado es: {pivote}\033[0m")
                return pivote

            if pivote.direccion > primer_parametro:
                der = med - 1
            else:
                izq = med + 1
        else:
            if pivote.codigo_postal == primer_parametro:
                print(f"\n\033[92m El envío encontrado es: {pivote}\033[0m")
                return pivote
            if pivote.codigo_postal > primer_parametro:
                der = med - 1
            else:
                izq = med + 1

    print("\n\033[92m ¡No se ha encontrado el envío!\033[0m")


def buscar_cp_fp(v, buscar_cp):
    """
    Funcion que busca un envío por código postal en el vector de envíos
    y muestra su importe final. Luego, actualiza la forma de pago del envío
    y muestra su nuevo importe final.

    Parametro v: Vector de envíos
    Parametro buscar_cp: Código postal a buscar
    Retorna el vector actualizado
    """
    envio = busqueda_binaria(v, buscar_cp)
    if not envio:
        return
    if int(envio.forma_pago) == 1:
        envio.forma_pago = "2"
    else:
        envio.forma_pago = "1"
    print(f"\n\033[92m Se actualizo la forma de pago: \n{envio}\033[0m")
    return v


def principal():
    opcion = -1
    v = []
    tipo = "HC"
    vector_importe = []
    may_imp = imp_menor = 0
    se_cargo_archivo = False
    while opcion != 0:
        opcion = menu()

        if opcion == 1:
            if len(v) > 0:
                print("\033[91mADVERTENCIA: ¡El vector tiene datos!\033[0m")
                borrar = input(
                    "¿Desea sobreescribir el mismo? (si: 0, no: 1) ")
                while not borrar.isnumeric() or int(borrar) < 0 or int(borrar) > 1:
                    print("\n\033[91m ¤ ¡Opcion no valida! ¤ \033[0m\n")
                    borrar = input(
                        "¿Desea sobreescribir el mismo? (si: 0, no: 1) ")
                if int(borrar) == 1:
                    continue
            se_cargo_archivo = True
            v, tipo = procesar_archivo()
            input("\nIngrese cualquier tecla para continuar...")

        elif opcion == 2:
            carga_manual(v)
            se_cargo_archivo = False
            input("\nIngrese cualquier tecla para continuar...")

        elif opcion == 3:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                input("\nIngrese cualquier tecla para continuar...")
                continue
            mostrar_vector(v)
            input("\nIngrese cualquier tecla para continuar...")

        elif opcion == 4:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                input("\nIngrese cualquier tecla para continuar...")
                continue

            buscar_direccion = input(
                "Por favor, introduzca la dirección a buscar (Debe terminar en .): ")
            while not buscar_direccion:
                print("\n\033[91m ¤ ¡Ingrese una dirección! ¤ \033[0m\n")
                buscar_direccion = input(
                    "Por favor, introduzca la dirección a buscar (Debe terminar en .): ")

            buscar_tipo_env = input(
                "Por favor, introduzca el tipo de envío a buscar: ")
            while not buscar_tipo_env.isnumeric() or \
                    int(buscar_tipo_env) < 0 or int(buscar_tipo_env) > 6:
                print("\n\033[91m ¤ ¡Opcion no valida! ¤ \033[0m\n")
                buscar_tipo_env = input(
                    "Por favor, introduzca el tipo de envío a buscar: ")

            if se_cargo_archivo:
                v_direccion = selection_sort(v, "direccion")
                busqueda_binaria(
                    v_direccion, buscar_direccion, buscar_tipo_env)
                input("\nIngrese cualquier tecla para continuar...")
                continue
            busqueda_lineal(v, buscar_direccion, buscar_tipo_env)
            input("\nIngrese cualquier tecla para continuar...")

        elif opcion == 5:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                input("\nIngrese cualquier tecla para continuar...")
                continue

            buscar_cp = input(
                "Por favor, introduzca el Código Postal a buscar: ")
            while not buscar_cp:
                print("\n\033[91m ¤ ¡Ingrese un Código Postal! ¤ \033[0m\n")
                buscar_cp = input(
                    "Por favor, introduzca el Código Postal a buscar: ")
            v_actualizado = buscar_cp_fp(v, buscar_cp)
            if v_actualizado is not None:
                v = v_actualizado

        elif opcion == 6:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                input("\nIngrese cualquier tecla para continuar...")
                continue
            cant_envios(v, tipo)
            input("\nIngrese cualquier tecla para continuar...")

        elif opcion == 7:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                input("\nIngrese cualquier tecla para continuar...")
                continue
            vector_importe = importe_final(v, tipo)
            input("\nIngrese cualquier tecla para continuar...")

        elif opcion == 8:
            if len(vector_importe) == 0:
                print(
                    "\n\033[91mADVERTENCIA: ¡Debe calcular los importes"
                    " finales de los envios!\033[0m")
                input("\nIngrese cualquier tecla para continuar...")
                continue
            may_imp = may_importe(vector_importe)
            porcentaje(vector_importe, may_imp)
            input("\nIngrese cualquier tecla para continuar...")

        elif opcion == 9:
            if len(vector_importe) == 0:
                print(
                    "\n\033[91mADVERTENCIA: ¡Debe calcular los importes"
                    " finales de los envios!\033[0m")
                input("\nIngrese cualquier tecla para continuar...")
                continue
            imp_menor = promedio_importe(vector_importe)
            menor_importe(vector_importe, imp_menor)
            input("\nIngrese cualquier tecla para continuar...")

        elif opcion == 0:
            print("\n\033[92m ¡HASTA LUEGO! \033[0m")


if __name__ == "__main__":
    principal()
