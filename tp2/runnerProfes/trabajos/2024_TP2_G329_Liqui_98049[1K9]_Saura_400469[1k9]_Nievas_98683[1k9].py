NOMBRE_ARCHIVO = "envios.txt"


def check_cars(linea, car1, car2):
    bandera_car1 = False
    for car in linea:
        if bandera_car1 and car in car2:
            return True
        bandera_car1 = False
        if car in car1:
            bandera_car1 = True
    return False


def datos(linea):
    cp = linea[:9].strip()
    direc = linea[9:29].strip()
    env = linea[29].strip()
    pago = linea[30].strip()
    return cp, direc, env, pago


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


def destinos(cp, cont_env_exterior=0):
    """ 1. Indicar el nombre del país de destino basado en el formato de los CP de Argentina y
        sus países vecinos. Si el CP no coincide con ninguno de estos formatos, se debe informar
        que el país es "Otro". 
    """
    if cp[0].isdigit():
        if len(cp) == 9 and cp[:5].isdigit() and cp[5] == "-" and cp[6:10].isdigit():
            destino = "Brasil"
        elif cp.isdigit():
            if len(cp) == 4:
                destino = "Bolivia"
            elif len(cp) == 7:
                destino = "Chile"
            elif len(cp) == 6:
                destino = "Paraguay"
            elif len(cp) == 5:
                destino = "Uruguay"
            else:
                destino = "Otro"
        else:
            destino = "Otro"
    # 2. Si el envío es dentro de Argentina, mostrar el nombre de la provincia de destino según
    #    el estándar ISO 3166-2:AR. Si el envío es internacional o
    #   hacia otro lugar fuera de Argentina, mostrar "No aplica".
    else:
        if cp[0] != "I" and cp[0] != "O" and len(cp) == 8 and cp[1:5].isdigit():
            destino = "Argentina"
        else:
            destino = "Otro"
    if destino != "Argentina":
        cont_env_exterior += 1
    return destino, cont_env_exterior


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


def cont_cartas(env, carta_simple, carta_certificada, carta_expresa):
    envio = int(env)
    if 0 <= envio <= 2:
        carta_simple += 1
    if envio in (3, 4):
        carta_certificada += 1
    if envio in (5, 6):
        carta_expresa += 1
    return carta_simple, carta_certificada, carta_expresa


def calc_porcentaje(envios, exterior):
    if envios == 0:
        return 0
    return int((exterior / envios) * 100)


def mayor_carta(ccs, ccc, cce):
    if ccs >= ccc and ccs >= cce:
        carta_mayor = "Carta Simple"
    elif ccc >= ccs and ccc >= cce:
        carta_mayor = "Carta certificada"
    else:
        carta_mayor = "Carta expresa"
    return carta_mayor


def cant_env_bs(cp, env, pago, destino, cont_env_bs, imp_bs):
    if destinos(cp)[0] == "Argentina" and cp[0] in "bB":
        cont_env_bs += 1
        imp_bs += calc_imp(cp, env, pago, destino)
    return cont_env_bs, imp_bs


def main():
    texto = open(NOMBRE_ARCHIVO, "rt", encoding="utf-8")
    linea = texto.readline()
    control = "No se especifico ningun control de dirección"
    cedvalid = cedinvalid = 0
    imp_acu_total = 0
    primer_cp, cant_primer_cp = None, 0
    ccs = ccc = cce = 0
    tipo_mayor = None
    menimp, mencp = 0, ""
    prom = 0
    cont_env = 0
    cont_env_bs = imp_bs = 0
    men_imp_br, men_cp_br, bandera_pr_imp_br = 0, "", True
    if check_cars(linea, 'hH', 'cC'):
        control = "Hard Control"
    if check_cars(linea, 'sS', 'cC'):
        control = "Soft Control"
    while linea != "":
        linea = texto.readline()
        if linea != "":
            cp, direc, env, pago = datos(linea)
            if control == "Hard Control":
                if valid_direc(direc):
                    cedvalid += 1
                    destino, cont_env = destinos(cp, cont_env)
                    imp_acu_total += calc_imp(cp, env, pago, destino)
                    cont_env_bs, imp_bs = cant_env_bs(
                        cp, env, pago, destino, cont_env_bs, imp_bs)
                    ccs, ccc, cce = cont_cartas(env, ccs, ccc, cce)
                    tipo_mayor = mayor_carta(ccs, ccc, cce)
                else:
                    cedinvalid += 1
            # Soft Control
            else:
                cedvalid += 1
                destino, cont_env = destinos(cp, cont_env)
                imp_acu_total += calc_imp(cp, env, pago, destino)
                cont_env_bs, imp_bs = cant_env_bs(
                    cp, env, pago, destino, cont_env_bs, imp_bs)
                ccs, ccc, cce = cont_cartas(env, ccs, ccc, cce)
                tipo_mayor = mayor_carta(ccs, ccc, cce)
            # Ignorar el control de direcciones
            if primer_cp is None:
                primer_cp = cp
            if cp == primer_cp:
                cant_primer_cp += 1
            if destinos(cp)[0] == 'Brasil':
                total_imp = calc_imp(cp, env, pago, 'Brasil')
                if bandera_pr_imp_br:
                    men_imp_br = total_imp
                    men_cp_br = cp
                    bandera_pr_imp_br = False
                if men_imp_br > total_imp:
                    men_imp_br = total_imp
                    men_cp_br = cp
            menimp = men_imp_br
            mencp = men_cp_br
    porc = calc_porcentaje(cedvalid + cedinvalid, cont_env)
    if cont_env_bs > 0:
        prom = int(imp_bs / cont_env_bs)
    print(' (r1) - Tipo de control de direcciones:', control)
    print(' (r2) - Cantidad de envios con direccion valida:', cedvalid)
    print(' (r3) - Cantidad de envios con direccion no valida:', cedinvalid)
    print(' (r4) - Total acumulado de importes finales:', imp_acu_total)
    print(' (r5) - Cantidad de cartas simples:', ccs)
    print(' (r6) - Cantidad de cartas certificadas:', ccc)
    print(' (r7) - Cantidad de cartas expresas:', cce)
    print(' (r8) - Tipo de carta con mayor cantidad de envios:', tipo_mayor)
    print(' (r9) - Codigo postal del primer envio del archivo:', primer_cp)
    print('(r10) - Cantidad de veces que entro ese primero:', cant_primer_cp)
    print('(r11) - Importe menor pagado por envios a Brasil:', menimp)
    print('(r12) - Codigo postal del envio a Brasil con importe menor:', mencp)
    print('(r13) - Porcentaje de envios al exterior sobre el total:', porc)
    print('(r14) - Importe final promedio de los envios Buenos Aires:', prom)


main()
