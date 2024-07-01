
# Sala de Chat con Sockets en Python


El proyecto consiste en un sistema de chat utilizando sockets en Python. El objetivo es permitir la comunicación entre múltiples clientes al conectarse a un servidor de chat.

# Requisitos
- Python

# Archivos

- server.py
- cliente.py

# Instrucciones

Encender el servidor
-
- Abrir el CMD u otra terminal.
- Navegar hasta el directorio donde está el archivo server.py.
- Ejecutar el comando ''python server.py'' para inicializar el servidor.

Conectarse como cliente
-
- Abrir un nuevo CMD u otra terminal.
- Navegar hasta el directorio donde está el archivo server.py.
- Ejecutar el comando ''python cliente.py'' para inicializar el servidor.
- Ingresar el puerto del servidor
- Ingresar username.


# Adicional
El puerto del servidor está configurado por defecto en 1024. Es modificable en la variable ''PUERTO'' en el archivo ''server.py''.

El buffer para recibir datos está configurado en 300 bytes. Tanto en el archivo de ''server.py'' como en ''cliente.py'' se puede modificar en la variable ''BUFFER_SIZE''



