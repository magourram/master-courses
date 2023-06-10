### perchè un sd deve essere trasparente, cosa vuol dire e che tipi di trasparenza ci sono

Ci sono 7 tipi di trasparenza:

Accesso: come si accede alla risorsa e come i dati sono rappresentati
Locazione: dove sono e come sono suddivisi i dati
Replicazione: se i dati sono replicati
Migrazione: una risorsa potrebbe essere spostata
Rilocazione: una risorsa potrebbe essere spostata mentre in uso
Concorrenza: nascorderla
Fallimento: nasconderlo

### cosa distingue un sist cluster da uno cloud o grid?

Un sistema di cluster, cloud e grid sono tutti modelli di elaborazione distribuita, ma hanno alcune differenze significative:

Cluster: Un cluster è costituito da un gruppo di computer (nodi) che lavorano insieme come una singola entità per eseguire carichi di lavoro complessi. I nodi in un cluster sono molto vicini fisicamente e comunicano tra loro tramite una rete ad alta velocità e bassa latenza. I cluster sono utilizzati principalmente per elaborazioni scientifiche, simulazioni o applicazioni di intelligenza artificiale.

Cloud: Il cloud computing è un modello di elaborazione distribuita in cui le risorse informatiche, come server, reti e archiviazione, sono fornite su richiesta via Internet. Il cloud computing è altamente scalabile e può fornire risorse informatiche in modo elastico, cioè aumentando o riducendo le risorse in base alla domanda. Il cloud computing è ampiamente usato per fornire servizi e applicazioni web.

Grid: Un sistema di griglia è una collezione di risorse informatiche eterogenee (come computer, storage e sensori) distribuiti geograficamente in una vasta area. Una griglia è progettata per condividere risorse tra organizzazioni, istituti o individui. La principale caratteristica della griglia è l’ampio coinvolgimento delle risorse disponibili. Ciò significa che le risorse provenienti da diverse organizzazioni possono essere utilizzate per eseguire un’applicazione particolare. Questo modello di elaborazione distribuita è utile per le applicazioni di ricerca.

In sintesi, i cluster sono gruppi di computer fisicamente vicini, i cloud sono servizi di elaborazione distribuita forniti su richiesta tramite Internet, mentre le griglie sono collezioni di risorse informatiche distribuite in un’ampia area e condivise tra diverse organizzazioni.

### distribuzione dei task tra client e server

Nelle architetture distribuite, il compito di elaborare i dati e fornire i risultati è spesso suddiviso tra client e server. In linea generale, il server gestisce la parte più pesante dell’elaborazione dei dati o delle richieste, mentre il client si occupa dell’interfaccia utente e della raccolta di informazioni da esso.

Ci sono vari modi di distribuire i task tra il client e il server. Alcuni esempi includono:

Client-driven: Nel modello client-driven, il client invia richieste specifiche al server e il server risponde con i dati richiesti. In questo modello, il client è il driver dell’elaborazione dei dati e il server è responsabile di soddisfare le richieste del client. Questo modello è comunemente utilizzato in applicazioni web, dove le richieste dell’utente vengono soddisfatte dal server.

Server-driven: Nel modello server-driven, il server inizia l’elaborazione dei dati e invia i risultati al client. In questo modello, il server è la fonte dell’iniziativa nell’elaborazione dei dati e il client è responsabile di ricevere e visualizzare i dati eventualmente elaborati. Questo modello è comunemente utilizzato in applicazioni client-server, dove il server fornisce servizi per la gestione dei dati.

Peer-to-peer: Nel modello peer-to-peer, ogni nodo (client o server) condivide le sue risorse con altri nodi. In questo modello, non ci sono server centralizzati o client, ma invece i nodi comunicano tra loro allo stesso livello. Questo modello è comunemente utilizzato in applicazioni come la condivisione di file peer-to-peer o le criptovalute, dove i nodi della rete collaborano spesso.

In ogni caso, la distribuzione dei task tra client e server dipende dalle esigenze specifiche dell’applicazione, dalle risorse disponibili dei nodi della rete, nonché dai limiti di comunicazione e dal tempo di risposta previsto.

### differenza overlay network strutturato / non strutturato e vantaggi/svantaggi di quello strutturato

In un’architettura peer-to-peer (P2P), un overlay network consente la comunicazione tra i nodi della rete su una connessione fisica sottostante e offre anche una struttura logica che supporta la ricerca e il routing dei dati tra i nodi. Ci sono due tipi di overlay network: strutturati e non strutturati.

Un overlay network strutturato è caratterizzato da una struttura ben definita. Questa struttura definisce un algoritmo di distribuzione dei dati tra i nodi della rete. Ci sono due tipi comuni di overlay network strutturati: cercatori di reti e anelli.

Un overlay network non strutturato, al contrario, non ha una struttura logica ben definita. I dati in un overlay network non strutturato vengono distribuiti casualmente tra i nodi della rete.

Il principale vantaggio di un overlay network strutturato è il routing efficiente e prevedibile dei dati. Utilizzando un protocollo di routing ben definito, un overlay network strutturato garantisce che ogni nodo abbia familiarità con la posizione approssimativa di un dato in base a un ID univoco. Ciò consente una ricerca efficiente e prevedibile di dati all’interno della rete.

Tuttavia, l’overlay network strutturato ha anche alcuni svantaggi. Ad esempio, il posizionamento efficiente dei dati dipende dall’ID dell’elemento in questione. Ciò può influire sulla distribuzione del carico nella rete, rendendo alcuni nodi sovraccarichi e altri sottoutilizzati. Inoltre, un overlay network strutturato richiede un overhead maggiore rispetto a un overlay non strutturato, in quanto richiede strumenti aggiuntivi per gestire la distribuzione dei dati e il routing tra i nodi.

In sintesi, un overlay network strutturato fornisce un routing efficiente dei dati e una struttura ben definita, il che può aiutare a garantire un’elaborazione efficiente dei dati. Tuttavia, richiede anche un overhead maggiore rispetto a un overlay network non strutturato e potrebbe influire sulla distribuzione del carico nella rete.

### le configurazioni possibili dei modelli di comunicazione (sincronia, persistenza, …)

Esistono diverse configurazioni possibili dei modelli di comunicazione, in cui la sincronia, la persistenza e lo stile di comunicazione sono importanti:

Sincrono e asincrono: la sincronia si riferisce all’allineamento temporale di mittente e destinatario nella comunicazione. In un’interazione sincrona, il mittente aspetta la conferma dal destinatario prima di procedere. In un’interazione asincrona, il mittente non aspetta una risposta immediata dal destinatario e può continuare la propria elaborazione senza attendere il risultato della comunicazione.

Persistente e non persistente: la persistenza si riferisce al tempo di vita di un messaggio. In una comunicazione persistente, il messaggio viene archiviato e trattenuto finché non venga ricevuto dal destinatario, anche se la connessione tra mittente e destinatario viene interrotta. In una comunicazione non persistente, il mittente invia il messaggio al destinatario solo se c’è un canale di comunicazione disponibile tra i due, e se questo non è possibile il messaggio non viene archiviato.

Orientato al flusso e orientato alla sessione: lo stile di comunicazione si riferisce al tipo di connessione tra mittente e destinatario durante la trasmissione del messaggio. In una comunicazione orientata al flusso, i dati vengono trasmessi come un flusso continuo senza sessione di connessione tra i vari pacchetti di dati. In una comunicazione orientata alla sessione, il mittente e il destinatario stabiliscono una connessione di sessione, in cui tutti i pacchetti sono trasmessi in un’unica sessione in modo ordinato e coerente.

Unicast, multicast e broadcast: questi termini definiscono il target del messaggio.

In una comunicazione unicast, un singolo messaggio viene inviato a un singolo destinatario.
In una comunicazione multicast, un messaggio viene inviato a più destinatari contemporaneamente, selezionati da un elenco di indirizzi di multicast.
In una comunicazione broadcast, un messaggio viene trasmesso a tutti i nodi della rete.
In sintesi, le configurazioni possibili dei modelli di comunicazione includono la sincronia/asincronia, la persistenza/non-persistenza, lo stile di comunicazione (orientato al flusso/orientato alla sessione) e il target del messaggio (unicast, multicast, broadcast). Il tipo di comunicazione che si adatta meglio a un determinato scenario dipende dalle esigenze specifiche dell’applicazione o del contesto in cui viene utilizzato.

### come sono le socket rispetto ai vari modelli di comunicazione? (sincronia? persistenza?)

Le socket sono una tecnologia software utilizzata per supportare la comunicazione tra applicazioni attraverso una rete. Le socket possono essere utilizzate per supportare tutti i modelli di comunicazione, inclusi i modelli synchroni/asynchroni, persistenti/non-persistenti e orientati al flusso o alla sessione.

In particolare, le socket supportano il modello di comunicazione asincrono (non bloccante), consentendo al mittente di inviare messaggi al destinatario senza dover aspettare una risposta immediata. Inoltre, le socket supportano la comunicazione persistente, anche in caso di interruzione della connessione di rete.

Nel modello di comunicazione orientato alla sessione, le socket vengono utilizzate per stabilire una connessione tra mittente e destinatario che dura per tutta la durata della sessione di comunicazione. Invece, nel modello orientato al flusso, le socket supportano l’invio di dati come un flusso continuo.

Per quanto riguarda il target del messaggio, le socket possono essere utilizzate per implementare il modello di comunicazione unicast (comunicazione punto a punto), ma anche il modello di comunicazione broadcast o multicast, dove il mittente invia i dati a più destinatari contemporaneamente.

### come si specifica la procedura degli stub (tecnicamente)? (linguaggio neutro…)

Ciò pone alcuni problemi: come faccio a chiamate una funzione con parametri
passati per riferimento(es. l’indirizzo del buffer)?
Sostanzialmente non si può, devo passare per valore, o comunque convertirli e serializzarli (Marshalling) e farli deserializzare al server (Unmarshalling).
Uno schema puo essere di chiamata a funzione remota sincrono. si può anche fare in modo asincrono. Per ottenere un risultato trasparente, uso i cosiddetti stubs, delle porzioni di codice in grado di chiamare la procedura remota inviando un messaggio al server, ricevendo una risposta una volta che quest’ultimo l’ha calcolata. Ma come faccio a fare il binding senza sapere IP,porte ecc? Esiste un server pubblico, il directory service, conosciuto sia dal client che dal server, al quale il client chiede l’indirizzo del server richiesto. Una volta scoperto l’indirizzo, contatto il daemon che gira nel server e lo risveglia in modo che mi possa restituire il suo endpoint.
Questa cosa si chiama binding RPC.
Un meccanismo simile a RPC è la Remote Object Invocation, la differenza sta nel fatto che i metodi chiamati in remoto vanno a modificare lo stato di un oggetto anziché restituire un risultato.

### qual è un modo alternativo a quello di un server perchè i nodi di un SD abbiano un orologio (quasi) preciso?

???

### NTP: come faccio a stimare ora giusta?

l’algoritmo NTP funziona in questo modo: il client invia richieste di sincronizzazione orario al server NTP impostato, che risponde fornendo l’ora corrente e il tempo impiegato per la trasmissione del messaggio. NTP quindi calcola il tempo di attesa ideale per la successiva richiesta di sincronizzazione in base alle informazioni ricevute dal server NTP. Poiché l’ora di riferimento a cui si sincronizzano i nodi può cambiare, NTP può anche effettuare un aggiornamento occasionale dell’ora di riferimento per garantire l’accuratezza continua della sincronizzazione.

L’utilizzo di NTP permette di mantenere gli orologi dei nodi in un sistema distribuito sincronizzati con un’accuratezza di frazioni di millisecondo, il che è importante per garantire l’accuratezza e l’affidabilità della comunicazione nel sistema distribuito.

### per risolvere il problema dell’esempio di compilazione con make, quale delle tre tipologie di sincronizzazione di clock è necessario per risolverlo

???

### process resiliance: come decido quanti processi avere in un gruppo?

Se k è il numero di processi che falliscono:
- Se ho solo il caso del crash da monitorare, allora bastano k+1 processi che
danno k fault tolerance (ne basta uno attivo x mandare avanti il sistema);
- Se ho response failure, mi servono almeno 2k+1 processi, e il client decide
votando: i server inviano al client le loro risposte, e il client decide in base
alla maggioranza.
- Se c’è bisogno di consenso nel gruppo (le decisioni vanno prese all’interno
del gruppo) la cosa è più complicata. Secondo Bettini servono, in una
situazione normale senza nodi malevoli, 3k+1 processi. In alcuni casi ciò è
impossibile, in particolare quando la maggioranza dei nodi sono malevoli
(dirigono la maggioranza verso di loro).


