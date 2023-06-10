// Consumer

public class ThreadPrintTerminal implements Runnable {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_RED = "\u001B[31m";
    
    private final Queue queue;
    private final String id;
    private final String ANSI_COLOR;

    public ThreadPrintTerminal(String id, Queue queue, String ANSI_COLOR) {
        this.id = id;
        this.queue = queue;
        this.ANSI_COLOR = ANSI_COLOR;
    }

    public void run() {
        while (true) {
            try {
                consume(queue.take());
            } catch (Exception e) { e.printStackTrace(); }
        }
    }

    public void consume(String message) {
        System.out.println(ANSI_COLOR + message + ANSI_RESET);
    }

} 
