import java.net.Socket;


public class Client {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_RED = "\u001B[31m";
    
    public static void main(String[] args) {
        
        try {
            Socket connectionSocket = new Socket("127.0.0.1", 1234);
 
            Queue queue = new Queue();
            Queue queue2 = new Queue();
            
            ThreadStandardInput si = new ThreadStandardInput("Client ThreadStandardInput", queue);
            ThreadSendSocket ss = new ThreadSendSocket("Client ThreadSendSocket", queue, connectionSocket);
            ThreadReceiveSocket rs = new ThreadReceiveSocket("Client ThreadReceiveSocket", queue2, connectionSocket);
            ThreadPrintTerminal pt = new ThreadPrintTerminal("Client ThreadPrintTerminal", queue2, ANSI_GREEN);

            new Thread(si).start();
            new Thread(ss).start();
            new Thread(rs).start();
            new Thread(pt).start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    
    }

} 
