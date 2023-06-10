// Producer

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class ThreadStandardInput implements Runnable {
    
    private final String id;
    private final Queue queue;

    public ThreadStandardInput(String id, Queue queue) { 
        this.id = id; 
        this.queue = queue; 
    }

    public void run() {
        String message;
        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
        while(true) try {
            message = inFromUser.readLine();                 
            queue.put(message);
        } catch (Exception e) { e.printStackTrace(); }
    }
}

