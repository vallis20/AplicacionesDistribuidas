import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class FileClient1 {
    public static void main(String[] args) {
        String serverAddress = "127.0.0.1"; // Dirección IP del servidor
        int serverPort = 12345; // Puerto del servidor

        try (Socket socket = new Socket(serverAddress, serverPort);
             DataInputStream dis = new DataInputStream(socket.getInputStream());
             DataOutputStream dos = new DataOutputStream(socket.getOutputStream())) {

            System.out.println("*****Selecciona una opcion:*****");
            System.out.println("1. Cargar Archivo");
            System.out.println("2. Descargar Archivo");
            
            // Crear un objeto Scanner para leer la entrada estándar (teclado)
            Scanner scanner = new Scanner(System.in);
             
            // Leer datos ingresados por el usuario
            String action = scanner.nextLine();

            // Enviar la acción al servidor
            dos.writeUTF(action);

            if (action.equals("1")) {
                // Nombre del archivo que deseas cargar
                String fileName = "archivo.txt";

                // Enviar el nombre del archivo al servidor
                dos.writeUTF(fileName);

                 // Obtener el tamaño del archivo
                File fileCarga = new File(fileName);
                long fileSize = fileCarga.length();
                dos.writeLong(fileSize);

                // Crear un flujo de entrada para el archivo
                FileInputStream fis = new FileInputStream(fileName);

                // Enviar el archivo al servidor
                byte[] buffer = new byte[8192];
                int bytesRead;
                while ((bytesRead = fis.read(buffer)) != -1) {
                    dos.write(buffer, 0, bytesRead);
                }
                fis.close();
                System.out.println("Archivo cargado: " + fileName);
            } else if (action.equals("2")) {
                // Nombre del archivo que deseas descargar
                String fileNameDescarga = "archivo.txt";

                // Enviar el nombre del archivo al servidor
                dos.writeUTF(fileNameDescarga);

                //Verificar si el archivo existe en el servidor
                boolean archivoExiste = dis.readBoolean();
                if (archivoExiste) {
                    // Obtener el tamaño del archivo
                    long fileSize = dis.readLong();
                    
                    // Crear un flujo de salida para guardar el archivo descargado
                    String rutaArchivoDescarga = "descargas" + File.separator + fileNameDescarga;
                    FileOutputStream fos = new FileOutputStream(rutaArchivoDescarga);
                    
                    // Recibir y guardar el archiv
                    byte[] buffer = new byte[8192];
                    int bytesRead;
                    long bytesReceived = 0;
                    while (bytesReceived < fileSize && (bytesRead = dis.read(buffer)) != -1) {
                        fos.write(buffer, 0, bytesRead);
                        bytesReceived += bytesRead;
                    }
                    fos.close();
                    System.out.println("Archivo descargado como: " + rutaArchivoDescarga);
                }else{
                    System.out.println("El archivo no existe en el servidor.");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
