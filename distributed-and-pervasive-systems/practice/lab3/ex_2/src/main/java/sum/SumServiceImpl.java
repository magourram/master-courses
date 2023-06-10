package sum;

import io.grpc.stub.StreamObserver;
import sum.Sum.*;
import sum.SumServiceGrpc.SumServiceImplBase;

public class SumServiceImpl extends SumServiceImplBase {
  
  @Override
  public void simpleSum(Numbers request, StreamObserver<Res> responseObserver) {

    // la richiesta è di tipo HelloRequest (definito in .proto)
    System.out.println(request);

    // costruisco la richiesta di tipo HelloResponse (sempre definito in .proto)
    Res response = Res.newBuilder().setRes(request.getV1() + request.getV2()).build();

    // passo la risposta nello stream
    responseObserver.onNext(response);

    // completo e finisco la comunicazione
    responseObserver.onCompleted();
  }

  // @Override
  // public void streamGreeting(HelloRequest request, StreamObserver<HelloResponse>
  // responseObserver){

  //    System.out.println("Metodo stream chiamato!");

  //    //la richiesta è di tipo HelloRequest (definito in .proto)
  //    System.out.println(request);

  //    //costruisco la richiesta di tipo HelloResponse (sempre definito in .proto)
  //    HelloResponse response = HelloResponse.newBuilder().setGreeting("Hello there,
  // "+request.getName()).build();

  //    //passo la risposta nello stream
  //    responseObserver.onNext(response);
  //    responseObserver.onNext(response);
  //    responseObserver.onNext(response);

  //    //completo e finisco la comunicazione
  //    responseObserver.onCompleted();

  // }

}
