package grpchelloserver;

import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;


public class App
{
    public static void main( String[] args )
    {
        //faccio partire il servizio sulla porta 8080
        try {

            Server server = ServerBuilder.forPort(8080).addService(new GreetingServiceImpl()).build();

            server.start();

            System.out.println("Server started!");

            server.awaitTermination();

        } catch (IOException e) {

            e.printStackTrace();

        } catch (InterruptedException e) {

            e.printStackTrace();

        }


    }
}
