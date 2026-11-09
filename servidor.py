import socket
from concurrent.futures import ThreadPoolExecutor

HOST = "localhost"
PUERTO = 5000

# Pool de 4 workers
workers = ThreadPoolExecutor(max_workers=4)


# Procesa la tarea enviada por el cliente
def procesar_tarea(tarea):
    return f"Resultado: {tarea.upper()}"


# Atiende a un cliente desde un worker
def manejar_cliente(cliente, direccion):
    print("Cliente conectado:", direccion[0])

    tarea = cliente.recv(1024).decode("utf-8")

    if tarea:
        resultado = procesar_tarea(tarea)
        cliente.sendall(resultado.encode("utf-8"))

    cliente.close()


# Configuración del servidor TCP/IP
def iniciar_servidor():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    servidor.bind((HOST, PUERTO))
    servidor.listen()

    print(f"Servidor escuchando en {HOST}:{PUERTO}")

    while True:
        cliente, direccion = servidor.accept()

        # La conexión se entrega a un worker del pool
        workers.submit(manejar_cliente, cliente, direccion)


if __name__ == "__main__":
    iniciar_servidor()
