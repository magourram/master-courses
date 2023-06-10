package ex2;

import java.net.ServerSocket;
import java.net.Socket;

class MultiServer {
    public static void main(String argv[]) throws Exception {
        int port = Integer.parseInt(argv[0]);
        ServerSocket welcomeSocket = new ServerSocket(port);
        Reservation reservation = new Reservation();

        while(true) {
            Socket connectionSocket = welcomeSocket.accept();

            // thread creation passing the established socket as arg
            TheatreServer theThread =
                    new TheatreServer(connectionSocket, reservation);

            // start of the thread
            theThread.start();
        }
    }
}