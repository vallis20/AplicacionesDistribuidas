import java.io.*;
import java.net.*;
import java.util.ArrayList;

public class ServidorJava {

    private static final int PORT = 52353;
    private static ArrayList<PrintWriter> clientes = new ArrayList<>();

    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(PORT);
            System.out.println("Servidor escuchando en el puerto " + PORT);

            while (true) {
                new ClientHandler(serverSocket.accept()).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static class ClientHandler extends Thread {
        private Socket socket;
        private PrintWriter out;

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        public void run() {
            try {
                out = new PrintWriter(socket.getOutputStream(), true);
                clientes.add(out);

                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                BufferedReader entradaConsola = new BufferedReader(new InputStreamReader(System.in));
                String mensajeCliente,mensajeServidor;
                while ((mensajeCliente = in.readLine()) != null) {
                    System.out.println("Cliente: " + mensajeCliente);
                    System.out.print("Servidor: ");
                mensajeServidor = entradaConsola.readLine();
                    enviarMensajeATodos(mensajeServidor);
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
                if (out != null) {
                    clientes.remove(out);
                }
                try {
                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }

        private void enviarMensajeATodos(String mensajeServidor) {
            for (PrintWriter cliente : clientes) {
                cliente.println(mensajeServidor);
            }
        }
    }
}
