def validador_numeros(num, min, max):
    while not num.isdigit() or int(num) < min or int(num) > max:
        num = input(f"Ingrese una opciòn entre {min} y {max}: ")
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
