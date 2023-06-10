package sum;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import sum.Sum.*;
import sum.SumServiceGrpc.*;

public class SumServiceClient {

  public static void main(String[] args) throws InterruptedException {

    System.out.println("Trying to call greeting synchronous method:\n");

    synchronousCall();

    System.out.println("\n...Done!");

    System.out.println("--------------");

    System.out.println("Now calling streamGreeting asynchronous method:\n");

    // asynchronousStreamCall();

    System.out.println("\n...Done!");
  }

  // calling a synchronous rpc operation
  public static void synchronousCall() {

    // plaintext channel on the address (ip/port) which offers the GreetingService service
    final ManagedChannel channel =
        ManagedChannelBuilder.forTarget("localhost:8080").usePlaintext().build();

    // creating a blocking stub on the channel
    SumServiceBlockingStub stub = SumServiceGrpc.newBlockingStub(channel);

    // creating the HelloResponse object which will be provided as input to the RPC method
    Numbers request = Numbers.newBuilder().setV1(3).setV2(4).build();

    // calling the method. it returns an instance of HelloResponse
    Res response = stub.simpleSum(request);

    // printing the answer
    System.out.println(response.getRes());

    // closing the channel
    channel.shutdown();
  }

  // calling an asynchronous method based on stream
  // public static void asynchronousStreamCall() throws InterruptedException {

  //    //plaintext channel on the address (ip/port) which offers the GreetingService service
  //    final ManagedChannel channel =
  // ManagedChannelBuilder.forTarget("localhost:8080").usePlaintext().build();

  //    //creating an asynchronous stub on the channel
  //    SumServiceStub stub = SumServiceGrpc.newStub(channel);

  //    //creating the HelloResponse object which will be provided as input to the RPC method
  //    Numbers request = Numbers.newBuilder().setV1(13).setV2(14).build();

  //    //calling the RPC method. since it is asynchronous, we need to define handlers
  //    stub.streamGreeting(request, new StreamObserver<HelloResponse>() {

  //        //this hanlder takes care of each item received in the stream
  //        public void onNext(HelloResponse helloResponse) {

  //            //each item is just printed
  //            System.out.println(helloResponse.getGreeting());

  //        }

  //        //if there are some errors, this method will be called
  //        public void onError(Throwable throwable) {

  //            System.out.println("Error! "+throwable.getMessage());

  //        }

  //        //when the stream is completed (the server called "onCompleted") just close the channel
  //        public void onCompleted() {

  //            channel.shutdownNow();

  //        }

  //    });

  //    //you need this. otherwise the method will terminate before that answers from the server are
  // received
  //    channel.awaitTermination(10, TimeUnit.SECONDS);

  // }

}
