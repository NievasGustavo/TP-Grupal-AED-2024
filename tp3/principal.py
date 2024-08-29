from funciones import procesar_archivo, carga_manual, mostrar_vector, \
    menu, cant_envios, importe_final, may_importe, \
    porcentaje, promedio_importe, menor_importe, buscar_tipo_direc


def principal():
    opcion = -1
    v = []
    tipo = "HC"
    vector_importe = []
    may_imp = imp_menor = 0
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
            v, tipo = procesar_archivo()

        elif opcion == 2:
            carga_manual(v)

        elif opcion == 3:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                continue
            mostrar_vector(v)

        elif opcion == 4:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                continue
            buscar_direccion = input(
                "Por favor, introduzca la dirección a buscar: ")
            buscar_tipo_env = input(
                "Por favor, introduzca el tipo de envío a buscar: ")
            while not buscar_tipo_env.isnumeric() or \
                    int(buscar_direccion) < 0 or int(buscar_direccion) > 6:
                print("\n\033[91m ¤ ¡Opcion no valida! ¤ \033[0m\n")
                buscar_tipo_env = input(
                    "Por favor, introduzca el tipo de envío a buscar: ")
            buscar_tipo_direc(v, buscar_direccion, buscar_tipo_env)

        elif opcion == 5:
            pass

        elif opcion == 6:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                continue
            cant_envios(v, tipo)

        elif opcion == 7:
            if len(v) == 0:
                print("\n\033[91mADVERTENCIA: ¡Cargue un envio!\033[0m")
                continue
            vector_importe = importe_final(v, tipo)

        elif opcion == 8:
            if len(vector_importe) == 0:
                print(
                    "\n\033[91mADVERTENCIA: ¡Debe calcular los importes"
                    " finales de los envios!\033[0m")
                continue
            may_imp = may_importe(vector_importe)
            porcentaje(vector_importe, may_imp)

        elif opcion == 9:
            if len(vector_importe) == 0:
                print(
                    "\n\033[91mADVERTENCIA: ¡Debe calcular los importes"
                    " finales de los envios!\033[0m")
                continue
            imp_menor = promedio_importe(vector_importe)
            menor_importe(vector_importe, imp_menor)
        elif opcion == 0:
            print("\n\033[92m ¡HASTA LUEGO! \033[0m")


if __name__ == "__main__":
    principal()
