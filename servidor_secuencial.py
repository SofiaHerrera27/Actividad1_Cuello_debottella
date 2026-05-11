import socket
import time

def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen(5)
    print("Servidor secuencial escuchando en el puerto 8000...")

    while True:
        cliente_socket, direccion = server_socket.accept()
        print(f"Conexión recibida de {direccion}")
        
        # Simulación de procesamiento pesado
        time.sleep(10) 
        
        cliente_socket.send("Respuesta: Procesamiento completado.\n".encode())
        cliente_socket.close()
        print(f"Conexión con {direccion} cerrada.")

if __name__ == "__main__":
    iniciar_servidor()
