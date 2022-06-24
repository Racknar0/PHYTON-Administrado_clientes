""" Administrador de clientes """

clients = []

# Añadimos mock data
marta = {'nombre': 'Marta', 'apellido': 'Pérez', 'dni': '15J'}
clients.append(marta)

# No hace falta crear la variable
clients.append({'nombre': 'Manolo', 'apellido': 'López', 'dni': '48H'})
clients.append({'nombre': 'Ana', 'apellido': 'García', 'dni': '28Z'})

if __name__ == '__main__':
    print(clients)