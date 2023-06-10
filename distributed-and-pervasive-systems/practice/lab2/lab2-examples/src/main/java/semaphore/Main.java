package semaphore;

import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String arg[]) throws Exception {
        Random r = new Random();
        ArrayList<Thread> threads = new ArrayList<Thread>();
        Semaphore s = new Semaphore(4);
        //create some threads
        for (int i=0; i<10; i++) {
            MyThread mt = new MyThread(r, i, s);
            threads.add(mt);
        }

        //start all the threads
        for (Thread t: threads) {
            t.start();
        }
    }
}

