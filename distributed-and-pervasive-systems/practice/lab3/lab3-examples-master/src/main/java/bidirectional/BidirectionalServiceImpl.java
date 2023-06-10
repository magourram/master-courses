package bidirectional;

import com.example.grpc.BidirectionalServiceGrpc.*;
import com.example.grpc.BidirectionalServiceOuterClass.*;
import io.grpc.stub.StreamObserver;


public class BidirectionalServiceImpl extends BidirectionalServiceImplBase {
    @Override
    public StreamObserver<ClientRequest> bidirectional(StreamObserver<ServerResponse> responseObserver){

        //it returns the stream that will be used by the clients to send messages. The client will write on this stream
        return new StreamObserver<ClientRequest>() {
            //receiving a message from the client
            public void onNext(ClientRequest clientRequest) {
                String clientStringRequest = clientRequest.getStringRequest();
                System.out.println("[FROM CLIENT] " + clientStringRequest);

                // sending the response to the client
                System.out.println("Sending the response to the client...\n");
                responseObserver.onNext(ServerResponse.newBuilder().setStringResponse("I've received this message: '" + clientStringRequest + "'").build());
            }

            public void onError(Throwable throwable) {
            }

            public void onCompleted() {
            }
        };
    }
}



