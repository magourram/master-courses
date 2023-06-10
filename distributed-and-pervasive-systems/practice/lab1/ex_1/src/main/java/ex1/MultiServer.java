package ex1;

import java.net.ServerSocket;
import java.net.Socket;

class MultiServer {
    public static void main(String argv[]) throws Exception {
        int port = Integer.parseInt(argv[0]);
        ServerSocket welcomeSocket = new ServerSocket(port);

        while(true) {
            Socket connectionSocket = welcomeSocket.accept();

            // thread creation passing the established socket as arg
            ServerThread theThread =
                    new ServerThread(connectionSocket);

            // start of the thread
            theThread.start();
        }
    }
}
