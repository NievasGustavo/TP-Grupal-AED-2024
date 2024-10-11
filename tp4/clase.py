class Envio:
    def __init__(self, cp, direc, tipo, fp):
        self.codigo_postal = cp
        self.direccion = direc
        self.tipo = tipo
        self.forma_pago = fp
        self.pais = determinar_pais(self.codigo_postal)
        self.importe = calc_imp(self.codigo_postal, self.tipo, self.forma_pago, self.pais)

    def __str__(self):
        r = "Código Postal: " + self.codigo_postal
        r += " - Dirección de destino: " + self.direccion
        r += " - Tipo de envio_pruebaío: " + str(self.tipo)
        r += " - Forma de pago: " + str(self.forma_pago)
        r += " - Pais: " + self.pais
        return r


def determinar_pais(cp):
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
    else:
        if cp[0] != "I" and cp[0] != "O" and len(cp) == 8 and cp[1:5].isdigit():
            destino = "Argentina"
        else:
            destino = "Otro"
    return destino


def calc_imp(cp, env, pago, destino):
    # 3. Calcular el importe inicial del envio_pruebaío.
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
            inicial = inicial * 1.20
        elif destino in ("Chile", "Uruguay"):
            inicial = inicial * 1.25
        elif destino == "Brasil":
            if 0 <= int(cp[0]) <= 3:
                inicial = inicial * 1.25
            elif 4 <= int(cp[0]) <= 7:
                inicial = inicial * 1.30
            else:
                inicial = inicial * 1.20
        else:
            inicial = inicial * 1.50
        # Calculamos el pago final, aplicando el descuento
        #  del 10% al importe inicial si es en efectivo
    if pago == "1":
        final = inicial * 0.90
    if pago == "2":
        final = inicial
    return round(final, 2)


if __name__ == "__main__":
    envio_prueba = Envio("6X626-325", "Oscar Freire 456.", "1", "1")
    print(envio_prueba)
    print(f"El importe es: {envio_prueba.importe}")
