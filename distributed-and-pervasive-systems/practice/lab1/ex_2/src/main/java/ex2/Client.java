package ex2;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.Socket;

public class Client {
    public static void main(String argv[]) throws Exception {

        // input stream initialization (from user keyboard)
        BufferedReader inFromUser =
                new BufferedReader(new InputStreamReader(System.in));

        //String address = inFromUser.readLine();
        //int port = Integer.parseInt(inFromUser.readLine());

        String address = argv[0];
        int port = Integer.parseInt(argv[1]);

		/* client socket initialization
			localhost: server address
			6789: server service port number */
        //Socket clientSocket = new Socket("localhost", 6789);
        Socket clientSocket = new Socket(address, port);


        // output stream towards socket initialization
        DataOutputStream outToServer =
                new DataOutputStream(clientSocket.getOutputStream());

        // input stream from socket initialization
        BufferedReader inFromServer =
                new BufferedReader(
                        new InputStreamReader(clientSocket.getInputStream()));

        // read a line from the user
        //sentence = inFromUser.readLine();

        System.out.println("Digit `buy` to buy a ticket: ");

        String buy = inFromUser.readLine();
        // String buy = "buy";

        System.out.println(buy);

        // send the line to the server
        outToServer.writeBytes(buy + '\n');

        // read the response from the server
        String result = inFromServer.readLine();
        System.out.println("FROM SERVER: " + result);
        clientSocket.close();
    }
}
