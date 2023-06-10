package semaphore;//Classe che implementa tramite wait e notify un Semaforo.
//Se non vi ricordate cosa sia un semaforo, google is your best friend.

public class Semaphore {
    private int maxNumber; //numero massimo di thread
    private int threadsIn; //conteggio dei thread nell'area critica

    Semaphore(int max) {
        maxNumber = max;
        threadsIn = 0;
    }

    public synchronized void enter() {
        System.out.println("" + threadsIn + " in the critical region...");
        //quando abbiamo raggiunto il numero massimo di thread, chi vuole entrare aspetta
        while (threadsIn >= maxNumber) {
            try {this.wait();}
            catch(InterruptedException ie) {ie.printStackTrace();}
        }

        threadsIn++;
    }

    public synchronized void exit() {
        threadsIn--;
        //quando un thread esce dall'area critica, sveglia qualcuno in attesa di entrare (se presente)
        this.notify();
    }
}

