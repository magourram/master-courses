import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String args[]) {
            Random rnd = new Random();
            int type;
            ArrayList<Thread> animals = new ArrayList<Thread>();
            WaitingRoom wr = new WaitingRoom();

            for(int i = 0; i < 10; i++) {
                type = rnd.nextInt(10) + 1;
                animals.add(new MyThread(type, wr));
            }

            System.out.println("Pre run");

            for(Thread animal : animals) {
                animal.run();
            }

            System.out.println("Post run");
    }
}
