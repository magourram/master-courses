package ex2;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

public class TheatreServer extends Thread {

    Reservation reservation;
    private Socket connectionSocket = null;
    private BufferedReader inFromClient;
    private DataOutputStream outToClient;

    public TheatreServer(Socket port, Reservation reservation) {
        connectionSocket = port;
        try {
            inFromClient =
                    new BufferedReader(
                            new InputStreamReader(connectionSocket.getInputStream()));
            outToClient =
                    new DataOutputStream(connectionSocket.getOutputStream());

        } catch (IOException e) {
            e.printStackTrace();
        }
        this.reservation = reservation;
    }


    public void run() {
        String buy;
        try {
            buy = inFromClient.readLine();
            if (buy.equals("buy")) {
                reservation.sell();
                outToClient.writeBytes("Sell tickets");
                System.out.println("Number of tickets: " + reservation.numberOfTickets);
                connectionSocket.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }


}
