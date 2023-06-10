public class MyThread extends Thread {
    private int type;
    private WaitingRoom wr;

    MyThread(int type, WaitingRoom wr) {
        // if type < 5: cat
        // else: dog
        this.type = type;
        this.wr = wr;
    }

    public void run() {
        System.out.println("RUN" + type);
        wr.enterRoom(type);

        System.out.println("ENTER" + type);
        try {
            this.sleep(1000);
            // Thread.sleep(1000);
            wr.exitRoom(type);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }

    }

}
