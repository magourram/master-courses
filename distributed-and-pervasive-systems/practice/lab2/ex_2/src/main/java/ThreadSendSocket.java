// Consumer

import java.io.DataOutputStream;
import java.net.Socket;

public class ThreadSendSocket implements Runnable {

    private final Queue queue;
    private final String id;
    private Socket connectionSocket;
    private DataOutputStream outToSocket; 
    
    public ThreadSendSocket(String id, Queue queue, Socket connectionSocket) {
        this.id = id;
        this.queue = queue;
        this.connectionSocket = connectionSocket;
    }

    public void run() {
        try {
            outToSocket = new DataOutputStream(connectionSocket.getOutputStream());
        } catch (Exception e) { e.printStackTrace(); }
        
        while (true) {
            consume(queue.take());
        }
    }

    public void consume(String message) {
        try {
            outToSocket.writeBytes(message + "\n");
        } catch (Exception e) { e.printStackTrace(); }
    }
}
