#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 23456
#define MAX_BUFFER_SIZE 1024

int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);
    char buffer[MAX_BUFFER_SIZE];

    // Crear el socket del servidor
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        perror("Error al crear el socket del servidor");
        exit(EXIT_FAILURE);
    }

    // Configurar la estructura del servidor
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    // Vincular el socket del servidor a la dirección y puerto
    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("Error al vincular el socket del servidor");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    // Escuchar por conexiones entrantes
    if (listen(server_socket, 5) == -1) {
        perror("Error al escuchar por conexiones entrantes");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("Esperando por conexiones entrantes...\n");

    // Aceptar una conexión entrante
    client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_len);
    if (client_socket == -1) {
        perror("Error al aceptar la conexión entrante");
        close(server_socket);
        exit(EXIT_FAILURE);
    }

    printf("Cliente conectado\n");

    // Leer y escribir datos desde/hacia el cliente
    while (1) {
        memset(buffer, 0, sizeof(buffer));
        int bytes_received = recv(client_socket, buffer, sizeof(buffer), 0);
        if (bytes_received <= 0) {
            perror("Error al recibir datos del cliente");
            break;
        }
        printf("Cliente: %s", buffer);

        memset(buffer, 0, sizeof(buffer));
        printf("Servidor: ");
        fgets(buffer, sizeof(buffer), stdin);
        send(client_socket, buffer, strlen(buffer), 0);
    }

    // Cerrar sockets
    close(client_socket);
    close(server_socket);

    return 0;
}
