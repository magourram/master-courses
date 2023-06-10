import java.io.*;

public class ProgrammingWithoutExceptions {
  public static void main(String[] args) {
    BufferedReader in = new BufferedReader(new FileReader("temp1.txt"));
    //BufferedReader in = new BufferedReader(new FileReader("temp.txt"));
    String line = in.readLine();
    int i = 1;
    while (line != null) {
      i++;
      line = in.readLine();
    }
    System.out.println("The file has " + (i - 1) + " rows.");
  }
}
