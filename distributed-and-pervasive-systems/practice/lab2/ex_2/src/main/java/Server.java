import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_RED = "\u001B[31m";
    
    public static void main(String[] args) {
        try {
            ServerSocket openSocket = new ServerSocket(1234);
            
            Socket connectionSocket = openSocket.accept();
            
            Queue queue = new Queue();
            Queue queue2 = new Queue();

            ThreadStandardInput si = new ThreadStandardInput("Server ThreadStandardInput", queue);
            ThreadSendSocket ss = new ThreadSendSocket("Server ThreadSendSocket", queue, connectionSocket);
            ThreadReceiveSocket rs = new ThreadReceiveSocket("Server ThreadReceiveSocket", queue2, connectionSocket);
            ThreadPrintTerminal pt = new ThreadPrintTerminal("Server ThreadPrintTerminal", queue2, ANSI_RED);
            
            new Thread(si).start();
            new Thread(ss).start();
            new Thread(rs).start();
            new Thread(pt).start();
        } catch (Exception e) { e.printStackTrace(); }
    }

} 
