def validador_numeros(num, min, max):
    while not num.isdigit() or int(num) < min or int(num) > max:
        num = input(f"Ingrese una opciòn entre {min} y {max}: ")
    return int(num)