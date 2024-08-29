import os.path


def country(cp):
    n = len(cp)
    if n < 4 or n > 9:
        return 'Otro'

    # ¿es Argentina?
    if n == 8:
        if cp[0].isalpha() and cp[0] not in 'IO' and cp[1:5].isdigit() and cp[5:8].isalpha():
            return 'Argentina'
        else:
            return 'Otro'

    # ¿es Brasil?
    if n == 9:
        if cp[0:5].isdigit() and cp[5] == '-' and cp[6:9].isdigit():
            return 'Brasil'
        else:
            return 'Otro'

    if cp.isdigit():
        # ¿es Bolivia?
        if n == 4:
            return 'Bolivia'

        # ¿es Chile?
        if n == 7:
            return 'Chile'

        # ¿es Paraguay?
        if n == 6:
            return 'Paraguay'

        # ¿es Uruguay?
        if n == 5:
            return 'Uruguay'

    # ...si nada fue cierto, entonces sea lo que sea, es otro...
    return 'Otro'


def check_dir(direccion):
    cl = cd = 0
    td = False
    ant = " "
    for car in direccion:
        if car in " .":
            # fin de palabra...
            # un flag si la palabra tenia todos sus caracteres digitos...
            if cl == cd:
                td = True

            # resetear variables de uso parcial...
            cl = cd = 0
            ant = " "

        else:
            # en la panza de la palabra...
            # contar la cantidad de caracteres de la palabra actual...
            cl += 1

            # si el caracter no es digito ni letra, la direccion no es valida... salir con False...
            if not car.isdigit() and not car.isalpha():
                return False

            # si hay dos mayusculas seguidas, la direccion no es valida... salir con False...
            if ant.isupper() and car.isupper():
                return False

            # contar digitos para saber si hay alguna palabra compuesta solo por digitos...
            if car.isdigit():
                cd += 1

            ant = car

    # si llegamos acá, es porque no había dos mayusculas seguidas y no habia caracteres raros...
    # ... por lo tanto, habria que salir con True a menos que no hubiese una palabra con todos digitos...
    # return True and td
    return td


def final_amount(cp, destino, tipo, pago):
    # determinación del importe inicial a pagar.
    importes = (1100, 1800, 2450, 8300, 10900, 14300, 17900)
    monto = importes[tipo]

    if destino == 'Argentina':
        inicial = monto
    else:
        if destino == 'Bolivia' or destino == 'Paraguay' or (destino == 'Uruguay' and cp[0] == '1'):
            inicial = int(monto * 1.20)
        elif destino == 'Chile' or (destino == 'Uruguay' and cp[0] != '1'):
            inicial = int(monto * 1.25)
        elif destino == 'Brasil':
            if cp[0] == '8' or cp[0] == '9':
                inicial = int(monto * 1.20)
            else:
                if cp[0] == '0' or cp[0] == '1' or cp[0] == '2' or cp[0] == '3':
                    inicial = int(monto * 1.25)
                else:
                    inicial = int(monto * 1.30)
        else:
            inicial = int(monto * 1.50)

    # determinación del valor final del ticket a pagar.
    # asumimos que es pago en tarjeta...
    final = inicial

    # ... y si no lo fuese, la siguiente será cierta y cambiará el valor...
    if pago == 1:
        final = int(0.9 * inicial)

    return final


def principal():
    # inicialización de variables auxiliares...
    # ...contadores para Resultados 2 y 3...
    cedvalid = cedinvalid = 0

    # ...acumulador para Resultado 4...
    imp_acu_total = 0

    # ...contadores para Resultados 5, 6 y 7...
    ccs = ccc = cce = 0

    # ...flag y contador para Resultados 9 y 10...
    first, cant_primer_cp, primer_cp = True, 0, "Ninguno"

    # ...variables para el menor importe final para Resultados 11 y 12...
    menimp, mencp = None, 'Ninguno'

    # ...contador de envios al exterior para Resultado 13...
    cext = 0

    # ...contador y acumulador para Resultado 14...
    ceba = aeba = 0

    # nombre del archivo de texto de entrada...
    # ... se asume que está en la misma carpeta del proyecto...
    fd = 'envios.txt'

    # control de existencia...
    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe...')
        print('Revise, y reinicie el programa...')
        exit(1)

    # procesamiento del archivo de entrada...
    # apertura del archivo...
    m = open(fd, 'rt')

    # procesamento de la línea de timestamp...
    # Resultado 1...
    line = m.readline()
    control = 'Soft Control'
    if 'HC' in line:
        control = 'Hard Control'

    # procesamiento de los envios registrados...
    while True:
        # ...intentar leer la linea que sigue...
        line = m.readline()

        # ...si se obtuvo una cadena vacia, cortar el ciclo y terminar...
        if line == '':
            break

        # ...procesar la línea leída si el ciclo no cortó...
        # ... obtener cada dato por separado, y en el tipo correcto...
        cp = line[0:9].strip().upper()
        direccion = line[9:29].strip()
        tipo = int(line[29])
        pago = int(line[30])

        # determinar el país de destino del envio...
        pais = country(cp)

        # importe final a pagar en ese envio...
        final = final_amount(cp, pais, tipo, pago)

        if control == "Hard Control":
            if check_dir(direccion):
                # Resultado 2: contar envios con direccion valida...
                cedvalid += 1

                # Resultado 4: acumulacion de importes finales de los envios con direccion valida...
                imp_acu_total += final

                # Resultados 5, 6 y 7: conteo de envios por tipo de carta (Hard control)...
                if tipo in (0, 1, 2):
                    # carta simple...
                    ccs += 1
                elif tipo in (3, 4):
                    # carta certificada...
                    ccc += 1
                else:
                    # carta expresa...
                    cce += 1

                # Resultado 13: contar envios al exterior para el porcentaje final (Hard control)...
                if pais != 'Argentina':
                    cext += 1

                # Resultado 14...
                # ...acumular importes finales y contar envios a Buenos Aires para el promedio (Hard Control)...
                if pais == 'Argentina' and cp[0] == 'B':
                    aeba += final
                    ceba += 1

            else:
                # Resultado 3: contar envios con direccion invalida...
                cedinvalid += 1

        else:
            # Resultados 2 y 3: Soft control: todas se cuentan como validas y el contador de invalidas queda en cero...
            cedvalid += 1

            # Resultado 4: Soft control: acumulacion de importes finales de todos los envios...
            imp_acu_total += final

            # Resultados 5, 6 y 7: conteo de envios por tipo de carta (Soft control)...
            if tipo in (0, 1, 2):
                # carta simple...
                ccs += 1
            elif tipo in (3, 4):
                # carta certificada...
                ccc += 1
            else:
                # carta expresa...
                cce += 1

            # Resultado 13: contar envios al exterior para el porcentaje final (Soft control)...
            if pais != 'Argentina':
                cext += 1

            # Resultado 14...
            # ...acumular importes finales y contar envios a Buenos Aires para el promedio (Soft Control)...
            if pais == 'Argentina' and cp[0] == 'B':
                aeba += final
                ceba += 1

        # Resultados 9 y 10...
        # ...detectar primer CP leido...
        if first is True:
            primer_cp = cp
            first = False

        # ...contar cuántas veces aparecio el primer CP...
        if cp == primer_cp:
            cant_primer_cp += 1

        # Resultados 11 y 12...
        if pais == 'Brasil':
            if menimp is None or final < menimp:
                menimp = final
                mencp = cp

    # cierre del archivo...
    m.close()

    # Resultado 8...
    if ccs >= ccc and ccs >= cce:
        tipo_mayor = 'Carta Simple'
    elif ccc >= cce:
        tipo_mayor = 'Carta Certificada'
    else:
        tipo_mayor = 'Carta Expresa'

    # Resultado 13...
    if control == "Hard Control":
        total_envios = cedvalid + cedinvalid
    else:
        total_envios = cedvalid

    porc = 0
    if total_envios != 0:
        porc = int(cext * 100 / total_envios)

    # Resultado 14...
    prom = 0
    if ceba != 0:
        prom = int(aeba / ceba)

    # visualización de resultados...
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
    print('(r14) - Importe final promedio de los envios a Buenos Aires:', prom)


# script principal...
if __name__ == '__main__':
    principal()
