package iterative;

import java.io.*;
import java.net.*;

class IterativeServer {
    public static void main(String argv[]) throws Exception {
        String clientSentence;
        String capitalizedSentence;

        // create a "listening socket" on the specified port
        ServerSocket welcomeSocket = new ServerSocket(6789);

        while(true) {
			/*	accept is a blocking call
				once a new connection arrived, it creates
				a new "established socket"	*/
            Socket connectionSocket = welcomeSocket.accept();

            // input stream from the socket initialization
            BufferedReader inFromClient =
                    new BufferedReader(
                            new InputStreamReader(connectionSocket.getInputStream()));

            // output stream to the socket initialization
            DataOutputStream outToClient =
                    new DataOutputStream(connectionSocket.getOutputStream());

            // read a line (that terminates with \n) from the client
            clientSentence = inFromClient.readLine();

            // wait for 10 seconds
            //Thread.sleep(10000);

            capitalizedSentence = clientSentence.toUpperCase() + '\n';

            // send the response to the client
            outToClient.writeBytes(capitalizedSentence);
        }
    }
}
