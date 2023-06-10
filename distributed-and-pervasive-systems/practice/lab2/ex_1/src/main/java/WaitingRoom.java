public class WaitingRoom {

    private int cats = 0;
    private int dogs = 0;

    WaitingRoom() {

    }

    synchronized public void enterRoom(int type) {
        while(true) {
            try {
                if (type <= 5) {
                    // Cats
                    if (cats > 1 || dogs > 1) {
                        this.wait();
                    } else {
                        cats++;
                        return;
                    }
                } else {
                    // Dogs
                    if (cats > 1) {
                        this.wait();
                    } else if (dogs > 4) {
                        this.wait();
                    } else {
                        dogs++;
                        return;
                    }
                }
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }
    }

    synchronized public void exitRoom(int type) {
        if (type <= 5) {
            // Cats
            cats--;
        } else {
            // Dogs
            dogs--;
        }
        this.notifyAll();
    }

}
