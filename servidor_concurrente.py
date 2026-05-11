import socket
import threading
import time

def manejar_cliente(cliente_socket, direccion):
    print(f" Atendiendo a {direccion} en un hilo nuevo...")
    # Simulación de carga pesada
    time.sleep(10)
    cliente_socket.send("Respuesta: Procesamiento multihilo exitoso.\n".encode())
    cliente_socket.close()
    print(f" Hilo para {direccion} finalizado.")

def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    print("Servidor CONCURRENTE (Multihilo) activo en puerto 8000...")

    while True:
        cliente_socket, direccion = server_socket.accept()
        # Creamos un hilo para cada cliente
        hilo = threading.Thread(target=manejar_cliente, args=(cliente_socket, direccion))
        hilo.start() # El hilo principal queda libre para aceptar al siguiente cliente
        print(f"Conexión de {direccion} delegada a un hilo trabajador.")

if __name__ == "__main__":
    iniciar_servidor()
