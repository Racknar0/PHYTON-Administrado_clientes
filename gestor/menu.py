""" Menú del programa """
import helpers

def loop():
    while True:
        helpers.clear()

        print("========================")
        print("  BIENVENIDO AL GESTOR  ")
        print("========================")
        print("[1] Listar clientes     ")
        print("[2] Mostrar cliente     ")
        print("[3] Añadir cliente      ")
        print("[4] Modificar cliente   ")
        print("[5] Borrar cliente      ")
        print("[6] Salir               ")
        print("========================")

        option = input("> ")

        helpers.clear()

        if option == '1':
            print("Listando los clientes...\n")
            # TODO
        if option == '2':
            print("Mostrando un cliente...\n")
            # TODO
        if option == '3':
            print("Modificando un cliente...\n")
            # TODO
        if option == '4':
            print("Modificando un cliente...\n")
            # TODO
        if option == '5':
            print("Borrando un cliente...\n")
            # TODO
        if option == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")