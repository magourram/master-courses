package student;

import it.ewlab.student.StudentOuterClass.*;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

    public static void main(String[] args) throws IOException {

        ServerSocket serverSocket = new ServerSocket(9999);

        Socket s = serverSocket.accept();

        Student st = Student.parseFrom(s.getInputStream());

        System.out.println(st);
    }


}
