from funciones import procesar_archivo, carga_manual, mostrar_vector, \
    menu, cant_envios, importe_final, may_importe, \
    porcentaje, promedio_importe, menor_importe, busqueda_lineal, busqueda_binaria, shellsort, buscar_cp_fp


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
                v_direccion = shellsort(v, "direccion")
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
