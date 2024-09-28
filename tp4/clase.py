class Envio:
    def __init__(self, cp, dir, tipo, fp):
        self.codigo_postal = cp
        self.direccion = dir
        self.tipo = tipo
        self.forma_pago = fp
        self.pais = determinar_pais(self.codigo_postal)

    def __str__(self):
        r = "Código Postal: " + self.codigo_postal
        r += " - Dirección de destino: " + self.direccion
        r += " - Tipo de envío: " + str(self.tipo)
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

if __name__ == "__main__":
    e = Envio("12345", "Calle 1", 1, 1)
    print(e)
