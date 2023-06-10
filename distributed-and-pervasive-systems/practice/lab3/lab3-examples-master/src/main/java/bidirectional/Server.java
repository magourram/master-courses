package bidirectional;

import io.grpc.ServerBuilder;
import java.io.IOException;

public class Server {
    public static void main( String[] args ) {
        try {
            io.grpc.Server server = ServerBuilder.forPort(8888).addService(new BidirectionalServiceImpl()).build();
            server.start();
            System.out.println("Server started!\n");
            server.awaitTermination();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
