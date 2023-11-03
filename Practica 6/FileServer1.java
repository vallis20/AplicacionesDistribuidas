import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class FileServer1 {
    public static void main(String[] args) {
        int port = 12345; // Puerto del servidor
        
        // Rutas de las carpetas de cargas y descargas
        String carpetaCargas = "cargas";
        String carpetaDescargas = "descargas";

        // Crea las carpetas si no existen
        File carpetaCargasDir = new File(carpetaCargas);
        carpetaCargasDir.mkdirs();
        File carpetaDescargasDir = new File(carpetaDescargas);
        carpetaDescargasDir.mkdirs();

        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("El servidor está escuchando en el puerto " + port);
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Cliente conectado desde " + clientSocket.getInetAddress().getHostAddress());

                try (DataInputStream dis = new DataInputStream(clientSocket.getInputStream());
                     DataOutputStream dos = new DataOutputStream(clientSocket.getOutputStream())) {

                    // Recibir la acción del cliente (cargar o descargar)
                    String action = dis.readUTF();

                    if (action.equals("1")) {
                        // El cliente desea cargar un archivo
                        String fileName = dis.readUTF();
                        long fileSize = dis.readLong();

                        // Ruta del archivo a cargar
                        String rutaArchivoCarga = carpetaCargas + File.separator + fileName;

                        // Crear un flujo de salida para el archivo
                        FileOutputStream fos = new FileOutputStream(rutaArchivoCarga);

                        // Recibir y guardar el archivo en el servidor
                        byte[] buffer = new byte[8192];
                        int bytesRead;
                        long bytesReceived = 0;
                        while (bytesReceived < fileSize && (bytesRead = dis.read(buffer, 0, (int) Math.min(buffer.length, fileSize - bytesReceived))) != -1) {
                            fos.write(buffer, 0, bytesRead);
                            bytesReceived += bytesRead;
                        }
                        fos.close();
                        System.out.println("Archivo cargado: " + fileName);
                    } else if (action.equals("2")) {
                        // El cliente desea descargar un archivo
                        String fileName = dis.readUTF();

                        // Ruta del archivo a descargar
                        String rutaArchivoDescarga = carpetaCargas + File.separator + fileName;

                        // Verificar si el archivo existe
                        File file = new File(rutaArchivoDescarga);
                        if (file.exists()) {
                            dos.writeBoolean(true); // Indicar que el archivo existe
                            dos.writeLong(file.length()); // Enviar el tamaño del archivo
                            dos.flush();

                            // Enviar el archivo al cliente
                            FileInputStream fis = new FileInputStream(file);
                            byte[] buffer = new byte[8192];
                            int bytesRead;
                            while ((bytesRead = fis.read(buffer)) != -1) {
                                dos.write(buffer, 0, bytesRead);
                            }
                            fis.close();
                            dos.flush();
                            System.out.println("Archivo enviado: " + fileName);
                        } else {
                            dos.writeBoolean(false); // Indicar que el archivo no existe
                            dos.flush();
                        }
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
