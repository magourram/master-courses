package bidirectional;

import com.example.grpc.BidirectionalServiceGrpc.*;
import com.example.grpc.BidirectionalServiceGrpc;
import com.example.grpc.BidirectionalServiceOuterClass.*;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.stub.StreamObserver;
import java.io.IOException;
import java.util.concurrent.TimeUnit;


public class Client {
    public final static String IP = "localhost";
    public final static int PORT = 8888;

    public static void main(String[] args) throws IOException {
        //opening a connection with server
        final ManagedChannel channel = ManagedChannelBuilder.forTarget(IP+":"+PORT).usePlaintext().build();

        //creating the asynchronous stub
        BidirectionalServiceStub stub = BidirectionalServiceGrpc.newStub(channel);

        //the stub returns a stream to communicate with the server.
        //the argument is the stream of messages which are transmitted by the server.
        StreamObserver<ClientRequest> serverStream = stub.bidirectional(new StreamObserver<ServerResponse>() {
            //remember: all the methods here are CALLBACKS which are handled in an asynchronous manner.

            //we define what to do when a message from the server arrives (just print the message)
            public void onNext(ServerResponse serverResponse) {
                System.out.println("[FROM SERVER] " + serverResponse.getStringResponse());
            }

            public void onError(Throwable throwable) {
            }

            public void onCompleted() {
            }
        });

        String msg = "First request from the client";
        System.out.println("Sending the message '" + msg + "' to the server...");
        serverStream.onNext(ClientRequest.newBuilder().setStringRequest(msg).build());

        msg = "Second request from the client";
        System.out.println("Sending the message '" + msg + "' to the server...");
        serverStream.onNext(ClientRequest.newBuilder().setStringRequest(msg).build());

        msg = "Third request from the client";
        System.out.println("Sending the message '" + msg + "' to the server...");
        serverStream.onNext(ClientRequest.newBuilder().setStringRequest(msg).build());



        try {
            //you need this. otherwise the method will terminate before that answers from the server are received
            channel.awaitTermination(10, TimeUnit.SECONDS);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}
