import sys
import socket
import threading

# Configuración
TCP_IP = '127.0.0.1'
BUFFER_SIZE = 300

# Definir función para obtener el puerto del usuario
def obtener_puerto():
    while True:
        puerto = input('Server: Ingresá un puerto (valor entre 1024-65535) o escribí "#salir" para finalizar: ')
        if puerto.lower() == '#salir':
            print('Server: Te desconectaste.')
            sys.exit()
        try:
            puerto = int(puerto)
            if 1024 <= puerto <= 65535:
                return puerto
            else:
                print('Server: Puerto fuera del rango.')
        except ValueError:
            print('Server: Ingresá un número válido.')

# Definir función para obtener el nombre de usuario
def obtener_nombre():
    while True:
        nombre = input('Ingresá tu user (en un rango de 3-10 caracteres) o escribí "#salir" para finalizar: ')
        if nombre.lower() == '#salir':
            print('Server: Programa finalizado.')
            sys.exit()
        if 3 <= len(nombre) <= 10:
            return nombre
        else:
            print('Server: El nombre no es válido.')

PUERTO = obtener_puerto()
NAME = obtener_nombre()

print(f"Server: {NAME} se está conectando a la sala de chat...")

try:
    socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_cliente.connect((TCP_IP, PUERTO))  # Conectarse al server
except socket.error as e:
    print(f"Error de conexión: {e}")
    sys.exit()

print(f"Server: {NAME} se conectó.")

# Definir función para recibir mensajes del server
def recibir_mensaje():
    while True:
        try:
            mensaje = socket_cliente.recv(BUFFER_SIZE)
            if not mensaje:
                raise ConnectionError
            print(mensaje.decode('utf-8'))  # Mostrar el mensaje recibido
        except ConnectionError:
            print("Server: Se cerró la conexión.")
            socket_cliente.close()
            sys.exit()

# Definir función para enviar mensajes al servidor
def enviar_mensaje():
    while True:
        try:
            mensaje_usuario = input()
            if mensaje_usuario == "#salir":
                mensaje = f"{NAME}: {mensaje_usuario}"
                socket_cliente.send(mensaje.encode('utf-8'))
                print("Server: Te has desconectado.")
                socket_cliente.close()
                sys.exit()
            mensaje = f"{NAME}: {mensaje_usuario}"
            if len(mensaje) > 150:  # Limitar cantidad de caracteres
                print("Server: Solo podés escribir 150 caracteres.")
                continue
            socket_cliente.send(mensaje.encode('utf-8'))  # Enviar el mensaje
        except ConnectionError:
            print("Server: Error enviando mensaje.")
            socket_cliente.close()
            sys.exit()

# Inicialización de hilos para enviar y recibir mensajes
enviar_thread = threading.Thread(target=enviar_mensaje, daemon=True)
obtener_thread = threading.Thread(target=recibir_mensaje, daemon=True)

enviar_thread.start()
obtener_thread.start()

# Mantener el programa en ejecución
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nServer: Programa finalizado por el usuario.")
    socket_cliente.close()
    sys.exit()
