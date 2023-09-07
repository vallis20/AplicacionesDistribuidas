#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define SERVER_IP "127.0.0.1"
#define PORT 23456
#define MAX_BUFFER_SIZE 1024

int main() {
    int client_socket;
    struct sockaddr_in server_addr;
    char buffer[MAX_BUFFER_SIZE];

    // Crear el socket del cliente
    client_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (client_socket == -1) {
        perror("Error al crear el socket del cliente");
        exit(EXIT_FAILURE);
    }

    // Configurar la estructura del servidor
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    inet_pton(AF_INET, SERVER_IP, &server_addr.sin_addr);

    // Conectar al servidor
    if (connect(client_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == -1) {
        perror("Error al conectar al servidor");
        close(client_socket);
        exit(EXIT_FAILURE);
    }

    printf("Conectado al servidor\n");

    // Leer y escribir datos desde/hacia el servidor
    while (1) {
        memset(buffer, 0, sizeof(buffer));
        printf("Cliente: ");
        fgets(buffer, sizeof(buffer), stdin);
        send(client_socket, buffer, strlen(buffer), 0);

        memset(buffer, 0, sizeof(buffer));
        int bytes_received = recv(client_socket, buffer, sizeof(buffer), 0);
        if (bytes_received <= 0) {
            perror("Error al recibir datos del servidor");
            break;
        }
        printf("Servidor: %s", buffer);
    }

    // Cerrar el socket del cliente
    close(client_socket);

    return 0;
}
