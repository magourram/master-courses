package ex1;

import java.io.*;
import java.net.*;

class Client {
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

        System.out.println("Add number: ");

        String number1 = inFromUser.readLine();
        String number2 = inFromUser.readLine();

        System.out.println(number1 + " " + number2);

        // send the line to the server
        outToServer.writeBytes(number1 + '\n');
        outToServer.writeBytes(number2 + '\n');

        // read the response from the server
        String result = inFromServer.readLine();
        System.out.println("FROM SERVER: " + result);
        clientSocket.close();
    }
}
