package ex1;

import java.io.*;
import java.net.*;

public class ServerThread extends Thread {
    private Socket connectionSocket = null;
    private BufferedReader inFromClient;
    private DataOutputStream outToClient;

    // the constructor argument is an established socket
    public ServerThread(Socket s) {
        connectionSocket = s;
        try {
            inFromClient =
                    new BufferedReader(
                            new InputStreamReader(connectionSocket.getInputStream()));
            outToClient =
                    new DataOutputStream(connectionSocket.getOutputStream());



        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void run() {
        String number;
        int sum = 0;
        try {
            number = inFromClient.readLine();
            sum += Integer.parseInt(number);
            number = inFromClient.readLine();
            sum += Integer.parseInt(number);

            //capitalizedSentence = number.toUpperCase() + '\n';

            outToClient.writeBytes(Integer.toString(sum));
            connectionSocket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
