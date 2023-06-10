package student;

import it.ewlab.student.StudentOuterClass.*;

import java.io.IOException;
import java.net.Socket;

public class Client {

    public static void main(String[] args) throws IOException {

        Socket s = new Socket("localhost", 9999);

        // Researcher r =
        //         Researcher.newBuilder()
        //                 .setName("Gabriele")
        //                 .setSurname("Civitarese")
        //                 .setType(Researcher.ResearcherType.POSTDOC)
        //                 .addPaper(Researcher.Paper.newBuilder().setTitle("Activity Recognition")
        //                         .setYear(2014).build())
        //                 .addPaper(Researcher.Paper.newBuilder().setTitle("Activity Recognition Again")
        //                         .setYear(2015).build())
        //                 .build();

        Student st =
                Student.newBuilder()
                        .setName("Gabriele")
                        .setSurname("Civitarese")
                        // .setType(Researcher.ResearcherType.POSTDOC)
                        
                        .addPlaceOfResidence(Student.Residence.newBuilder()
                                .setAddress("Via X")
                                .setNumber(10)
                                .build())
                        
                        .setYearOfBirth("2022")
                        .build();

        st.writeTo(s.getOutputStream());

        s.close();


    }
}
