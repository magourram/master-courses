// Producer

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

public class ThreadReceiveSocket implements Runnable {
    
    private final Queue queue;
    private final String id;
    private Socket connectionSocket;
    private BufferedReader inFromSocket; 
    
    public ThreadReceiveSocket(String id, Queue queue, Socket connectionSocket) {
        this.id = id;
        this.queue = queue;
        this.connectionSocket = connectionSocket;
    }

    public void run() {
        String message;
        try {
            inFromSocket = new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));

            while(true) {
                message = inFromSocket.readLine();
                queue.put(message);
            }
        } catch (IOException e) { e.printStackTrace(); }
    }
} 
