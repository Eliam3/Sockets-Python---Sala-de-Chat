import sys
import socket
import threading

# Configuración
TCP_IP = '127.0.0.1'
PUERTO = 1024
TAM_BUFFER = 300
clientes = []

# Definir función para el inicio del servidor
def main():
    global clientes
    print("Server: Iniciando servidor.")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind((TCP_IP, PUERTO))  # Vincular el socket al IP y puerto
        server_socket.listen(10)  # Limitar cantidad de conexiones
        print(f"Server: Escuchando en {TCP_IP}:{PUERTO}")
        while True:
            socket_cliente, addr = server_socket.accept()  # Aceptar nueva conexión
            clientes.append(socket_cliente)  # Añadir al cliente a la lista
            thread = threading.Thread(target=gestion_clientes, args=(socket_cliente, addr), daemon=True)
            thread.start()
            print(f"Server: Conexión con {addr} establecida.")
    except socket.error as e:
        print(f"Server: Puerto no disponible: {e}")
        sys.exit()
    finally:
        server_socket.close()  # Cerrar el socket del servidor
        print(f"Server: Cerrando socket {PUERTO}")

# Definir función para la gestión de clientes
def gestion_clientes(socket_cliente, direccion_cliente):
    global clientes
    try:
        while True:
            datos_recibidos = socket_cliente.recv(TAM_BUFFER)
            if not datos_recibidos:  # Se cierra la conexión si no hay datos recibidos
                print(f"Server: Conexión perdida con {direccion_cliente}.")
                break
            mensaje = datos_recibidos.decode('utf-8')  # Decodificar mensaje
            if "#salir" in mensaje:  # Desconexión del cliente
                print(f"Server: {direccion_cliente} se ha desconectado.")
                break
            for cliente in clientes:
                if cliente != socket_cliente:  # Enviar el mensaje a los clientes
                    try:
                        cliente.send(mensaje.encode('utf-8'))
                    except Exception as e:
                        print(f"Server: Error enviando mensaje a {cliente.getpeername()}: {e}")
    except ConnectionError as error:
        print(f"Server: Error de conexión con {direccion_cliente}: {error}")
    finally:
        socket_cliente.close()  # Cerrar el socket del cliente
        if socket_cliente in clientes:
            clientes.remove(socket_cliente)  # Eliminar al cliente de la lista
        print(f"Server: {direccion_cliente} desconectado.")

if __name__ == "__main__":
    main()
