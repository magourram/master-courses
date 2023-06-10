package join;

import java.util.Random;

public class MyThread extends Thread {
    private Random rnd;

    MyThread(Random r) {
        rnd = r;
    }

    public void run() {
        int seconds = rnd.nextInt(10) + 1;

        System.out.println("A thread started!");

        try
        {
            Thread.sleep(seconds * 1000);
        }
        catch(Exception ex)
        {
            ex.printStackTrace();
        }

        System.out.println("A thread died!");

    }

}
