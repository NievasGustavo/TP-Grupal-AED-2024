import subprocess
import os

# Directorio donde se almacenan los programas entregados por los estudiantes
SOURCES = "./trabajos/"

# Resultados esperados ("Expected Results") para el archivo envios25.txt...
# ER = ['Hard Control', '17', '8', '152627', '9', '3', '5', 'Carta Simple', '03X3076', '2', '2250', '07439-412', '60', '10900']

# Resultados esperados ("Expected Results") para el archivo envios100HC.txt...
# ER = ['Hard Control', '63', '37', '571649', '31', '15', '17', 'Carta Simple', '247X', '1', '1287', '65090-152', '54', '16110']

# Resultados esperados ("Expected Results") para el archivo envios100SC.txt...
# ER = ['Soft Control', '100', '0', '943197', '42', '34', '24', 'Carta Simple', '247X', '1', '1287', '65090-152', '86', '16110']

# Resultados esperados ("Expected Results") para el archivo envios500b.txt (de prueba para los estudiantes)...
# ER = ['Hard Control', '353', '147', '3325431', '160', '93', '100', 'Carta Simple', '482211', '6', '1237', '15735-587', '62', '13585']

# Resultados esperados ("Expected Results") para el archivo envios.txt (el que usaremos para el test)...
ER = ['Hard Control', '346', '154', '3495925', '141', '102', '103', 'Carta Simple', '499301', '7', '1237', '33366-042', '60', '2002']


# Muestra los valores contenidos en "text" en una línea de color rojo intenso.
def print_red(*text, end="\n"):
    for t in text:
        print(f"\033[91m{t}\033[00m", end=" ")
    print(end=end)


# Ejecuta el programa "script" y captura las salidas que sean dirigidas a la consola estándar.
def run(script):
    proc = subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return proc


def collect_results(lines):
    # ... recolectar los resultados desde la consola estándar...

    results = []
    for i in range(len(lines)):
        # ...los resultados vienen luego de una secuencia ': '...
        r = lines[i].split(': ')
        results.append(r[1].strip())

    # ...retornar los resultados y salir...
    return results


def show_and_count(lines, results, data):
    # Índice para recorrer la lista "data" de resultados...
    k = 0

    # Contador de resultados correctos...
    ok = 0

    for i in range(len(lines)):
        # ... mostrar el resultado tal como se mostró en el programa original...
        print("\t", lines[i], end="")

        # ... e informar correctos e incorrectos...
        if results[i].strip() == data[k]:
            ok += 1
            print(f"\033[92m --> Correcto\033[00m")
        else:
            print(f"\033[91m --> Incorrecto (esperado: {data[k]})\033[00m")

        k += 1

    # ...retornar el contador de respuestas correctas y salir...
    return ok


# Ejecuta el programa "script" enviado por los estudiantes, y analiza los resultados.
def start(script):
    print_red("\n---------------------------------")
    print_red("Programa:", script.name)
    print_red("---------------------------------")

    # Ejecutar el programa entregado por el estudiante...
    process = run(script.path)

    # Si hay datos tomados desde la línea de órdenes, en la variable data, va esta línea...
    # stdout_value = ended.communicate(data[0].encode('utf-8'))[0].decode('utf-8')

    # Si NO hay datos desde la línea de órdenes, va esta otra...
    # ...para capturar lo que sea que se haya enviado a la consola de salida...
    stdout_value = process.communicate()[0].decode('utf-8')

    # ...y dividir en líneas esa salida...
    lines = stdout_value.splitlines()

    # ...recolectar los resultados desde la consola estándar...
    results = collect_results(lines)

    # Mostrar las salidas del programa tal cual fueron generadas por los estudiantes...
    # ...pero indicando y contando los resultados correctos o no...
    ok = show_and_count(lines, results, ER)

    n = len(ER)
    prc = ok * 100 // n
    print()
    print(f"\033[95mCantidad de resultados correctos: {ok}\033[00m")
    print(f"\033[95mPorcentaje de resultados correctos: {prc}%\033[00m")


# Inicia el test para todos los programas contenidos en el directorio "SOURCES".
def init():
    with os.scandir(SOURCES) as programs:
        for script in programs:
            if script.name.endswith(".py"):
                try:
                    start(script)
                except Exception as ex:
                    print()
                    print(f"\033[1;93;41m--> Error al ejecutar: ({ex})\033[00m")
                print()
                # input("Presione <Enter> para continuar con el siguiente trabajo...")


if __name__ == '__main__':
    init()
