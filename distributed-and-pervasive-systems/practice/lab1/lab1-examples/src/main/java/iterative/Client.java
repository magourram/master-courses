package iterative;

import java.io.*;
import java.net.*;

class Client {
    public static void main(String argv[]) throws Exception {
        String sentence;
        String modifiedSentence;

        // input stream initialization (from user keyboard)
        BufferedReader inFromUser =
                new BufferedReader(new InputStreamReader(System.in));

		/* client socket initialization
			localhost: server address
			6789: server service port number */
        Socket clientSocket = new Socket("localhost", 6789);

        // output stream towards socket initialization
        DataOutputStream outToServer =
                new DataOutputStream(clientSocket.getOutputStream());

        // input stream from socket initialization
        BufferedReader inFromServer =
                new BufferedReader(
                        new InputStreamReader(clientSocket.getInputStream()));

        // read a line from the user
        sentence = inFromUser.readLine();

        // send the line to the server
        outToServer.writeBytes(sentence + '\n');

        // read the response from the server
        modifiedSentence = inFromServer.readLine();
        System.out.println("FROM SERVER: " + modifiedSentence);
        clientSocket.close();
    }
}
