""" Administrador de clientes """
import re
import helpers

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
    
    
    
    
def add():

    client = dict()

    print("Introduce nombre (De 2 a 30 caracteres)")
    client['nombre'] = helpers.input_text(2, 30)

    print("Introduce apellido (De 2 a 30 caracteres)")
    client['apellido'] = helpers.input_text(2, 30)

    while True:
        print("Introduce DNI (2 números y 1 carácter en mayúscula)")
        dni = helpers.input_text(3, 3)
        if is_valid(dni):
            client['dni'] = dni
            break
        print("DNI incorrecto o en uso")

    clients.append(client)
    return client    
    
    
def edit():
    dni = input("Introduce el DNI del cliente\n> ")
    for i, client in enumerate(clients):
        if client['dni'] == dni:
            print(f"Introduce nuevo nombre ({client['nombre']})")
            clients[i]['nombre'] = helpers.input_text(2, 30)
            print(f"Introduce nuevo apellido ({client['apellido']})")
            clients[i]['apellido'] = helpers.input_text(2, 30)
            return True
    return False


    
def is_valid(dni):
    """
    >>> is_valid('48H')  # No válido, en uso
    False
    >>> is_valid('X82')  # No válido, incorrecto
    False
    >>> is_valid('21A')  # Válido
    True
    """

    # Comprueba que el dni empieza con un patrón
    if not re.match('[0-9]{2}[A-Z]', dni):
        return False

    # Comprueba que el dni no esté repetido
    for client in clients:
        if client['dni'] == dni:
            return False

    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()