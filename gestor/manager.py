""" Administrador de clientes """

clients = []

# Añadimos mock data
marta = {'nombre': 'Marta', 'apellido': 'Pérez', 'dni': '15J'}
clients.append(marta)

# No hace falta crear la variable
clients.append({'nombre': 'Manolo', 'apellido': 'López', 'dni': '48H'})
clients.append({'nombre': 'Ana', 'apellido': 'García', 'dni': '28Z'})


def show(client):
    print(f"{client['dni']}: {client['nombre']} {client['apellido']}")


def show_all():
    for client in clients:
        show(client)
        

def find():

    dni = input("Introduce el DNI del cliente\n> ")

    for client in clients:
        if client['dni'] == dni:
            show(client)
            return client

    print("No se ha encontrado ningún cliente con ese DNI")