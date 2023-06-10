package researcher;

import it.ewlab.researcher.ResearcherOuterClass.Researcher;

import java.io.IOException;
import java.net.Socket;

public class Client {

    public static void main(String[] args) throws IOException {

        Socket s = new Socket("localhost", 9999);

        Researcher r =
                Researcher.newBuilder()
                        .setName("Gabriele")
                        .setSurname("Civitarese")
                        .setType(Researcher.ResearcherType.POSTDOC)
                        .addPaper(Researcher.Paper.newBuilder().setTitle("Activity Recognition")
                                .setYear(2014).build())
                        .addPaper(Researcher.Paper.newBuilder().setTitle("Activity Recognition Again")
                                .setYear(2015).build())
                        .build();

        r.writeTo(s.getOutputStream());

        s.close();


    }
}
