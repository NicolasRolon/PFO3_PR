import socket

HOST = "localhost"
PUERTO = 5000


while True:
    tarea = input('Ingrese una tarea o escriba "salir": ')

    if tarea.lower() == "salir":
        break

    # Crea una conexión con el servidor
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PUERTO))

        # Envía la tarea
        cliente.sendall(tarea.encode("utf-8"))

        # Recibe el resultado
        resultado = cliente.recv(1024).decode("utf-8")

        print("Servidor:", resultado)
