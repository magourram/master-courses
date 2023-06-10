package ex2;

public class Reservation {
    int numberOfTickets = 10;

    public void sell() {
        synchronized (this) {
            numberOfTickets--;
        }
    }


}
