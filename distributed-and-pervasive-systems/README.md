# Distributed and Pervasive Systems

## Introduction

- A distributed system is:

    A collection of independent computers that appears to its users as a single coherent system
    
    A distributed system organized as middleware. The middleware layer extends over multiple machines, and offers each application the same interface.

**Transparency in a Distributed System**

|Transparency|Description|
|-|-|
|Access|Hide differences in data representation and how a resource is accessed|
|Location|Hide where a resource is located|
|Migration|Hide that a resource may move to another location| 
|Relocation|Hide that a resource may move to another location while in use|
|Replication|Hide that a resource is replicated| 
|Concurrency|Hide that a resource may be shared by several competitive users|
|Failure|Hide the failure and recovery of a resource|

**Openness**

An open distributed system should offer interoperability, portability and extensibility. The openness can be achived by the use of standard protocols, the publication of key interfaces and testing and verifying the conformance of components to published standards.

**Scalability problem**

Characteristics of decentralized algorithms:

- No machine has complete information about the system state.
- Machines make decisions based only on local information.
- Failure of one machine does not ruin the algorithm.
- There is no implicit assumption that a global clock exists.

To increase scalability we want to let the server do as few operations as possible.

**Pitfalls when Developing Distributed Systems**

- The network is reliable.
- The network is secure.
- The network is homogeneous.
- The topology does not change.
- Latency is zero.
- Bandwidth is infinite.
- Transport cost is zero.
- There is one administrator.
- Debugging distributed applications is analogous to standard applications

## Distributed Computing Systems

**Cluster Computing Systems**

A collection of similar workstations/servers closely connected by high-speed local-area network and usually running the same operating system. The goal is high performance computing tasks, or high availability.

Asymmetric approach: A master node distributes tasks on a set of computing nodes.

Symmetric approach: There is no master, all nodes have the same software installed.

**Cloud Computing**

Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared pool of configurable computing resources that can be rapidly provisioned and released with minimal management effort or service provider interaction.

- The nodes are etherogenous in hardware and operating system.
- Network connections are etherogenous in their capacities and
reliability
- On-demand self-service. A consumer can unilaterally provision computing capabilities
- Broad network access. Capabilities are available over the network and accessed through standard mechanisms
- Resource pooling. The provider’s computing resources are pooled to serve multiple consumers
- Rapid elasticity. Capabilities can be elastically provisioned and released
- Measured service. Cloud systems automatically control and optimize resource use by leveraging a metering capability

**Edge (or Fog) Computing**

IoT: sensorized connected devices produce massive amounts of data that must often be processed in real time. There is a need for reliability and low latency.

Processing all data in the cloud does not meet stringent latency requirements. Communication to the cloud also requires energy.

“fog” isu used to refer to an intermediate level of decentralization between cloud and edge using more powerful nodes.

**Distributed Information Systems**

- Distributed Databases
- Transaction Processing Systems

ACID:

- Atomic: To the outside world, the transaction happens indivisibly.
- Consistent: The transaction does not violate system invariants.
- Isolated: Concurrent transactions do not interfere with each other.
- Durable: Once a transaction commits, the changes are permanent.

**Distributed Pervasive System**

A distributed system with the following main features:

- it includes unconventional nodes

- adaptivity

## Distributed Systems Architectures

 **Centralize architectures**

 - Client - Sererver architectures (request - response pattern)
 - Event Bus Architectures (Publish - subscribe pattern)

 Types of distribution:

- Vertical distribution: a different server/node for each functionality.
- Horizontal distribution: The same functionality is distributed on multiple servers/nodes with load balancing.
- Vertical and horizontal distribution: Each functionality duplicated on a separate group of servers with load balancing.

**Microservice architecture**

Pushing forward the vertical distribution, running each component/functionality of the application logic in a separate process, possibly on a separate machine.

- (micro)Services must be indipendently replacable and upgradable.
- (micro)Services communicate with lightweight mechanisms (REST or RPC).
- Focused Scalability: act on the specific (micro)Services that need to be scaled.
- (micro)Services may be written in different programming languages. 

**Container**

Abstraction at the application layer that packages code and dependencies together.

Virtualization at the process level in user space.

It offers efficient support for the microservice architecture.

It inscreases the portability, enabling easy migration and reducing problems at deployment time.

**Decentralize architecture**

Peer-to-peer model:

- All nodes have the same functional capabilities.
- Designed so that each user contributes resources.
- Operation does not depend on any centrally administreted system.

How does Napster work:

1. *File location request*, from client1 to Napster server
2. *List of peers offering the file*, Napster server to client1
3. *File request*, from client1 to client2
4. *File delivered*, from client2 to client1
5. *Index update*, from client2 to Napster server

### Overlay network

- Optimization criteria: global scalability, load balancing, locality of interfaction, suport of encryption and authentication, anonymity.
- P2P systems are often organized in an overlay network
- An overlay network is a logical network over an existing lower level network

Routing Overlay:

- A distributed algorithm to locate nodes and objects in an overlay network
- Routing requests from clients to host holding objects of interest at the application level instead of the network level.
- Routing is based on global identifiers and should direct to one of the replicas of the object.
- Routing overlay protocols also deal with insertion/removal of objects and nodes

*Structured overlay network*: Overlay Network deterministically built (often via hash table) in order to obtain efficient routing towards the node containing the required data. The limitation of structured overlay are maintenance of complex overlay structure can be difficultt and costly to achieve and need for self organizing nodes.

*Unstructured overlay network*: Overlay Network built with randomized algorithms, each peer knows only its neighbors, and sometimes they have a hierarchical structure through superpeer nodes

**Chord** (a P2P system with structured overlay)

There is a fixed address space, each node gets as id an address in the space and each data item gets a key in the same space.

A data item with key *k* is managed bu the first node with id >= *k*, called *succ(k)*

Chord provides LOOKUP(k) to efficiently find the address

Key resolution:

- Hash table of node with id = p
    - if m is the number of bits in the address space each table has m entries
    - HashTable(i) is the i-th entry of the table and stores the id and address of *succ(p + 2^{i-1})*
- Computing LOOKUP(k): *Suppose the search starts at node p and HashTable() is its finger table*
    - if k = p, the data is on p, otherwise the search is forwarded to a node q
    - if HashTable(j) <= k < HashTable(j+1), then q=HashTable(j)
    - if p < k and k < HashTable(1), then q=HashTable(1)
    - if k >= HashTable(m), then q=HashTable(m) 

Chord must update the routing information when a node joins or leaves the network and addresses of successor/predecessor nodes must be updated and resources must be moved and also the HashTable must be updated.

**CAN** (structured overlay)

Assignment of data to nodes in CAN and it uses a bi-dimensional address space. Each key is a point and each node manages all the point in its region.

**Google file system**

Motivations:

- Storage of very large files
- Use of large clusters of “commodity" computers
- Files are mostly read or appended to
- High data throughput desired

Files are divided into chunks with unique labels and distributed over chunkservers and a master node stres the metadata needed to map chunk labels to chunkservers.

## Communication models in distributed systems

**Types of communication**

Viewing middleware as an intermediate service in application-level communication.

Persistent: there is a server in between or a queue where store the messages 
Trasient: there is not a server in between
Asynchronous: the server does not send an ACK
Synchronous: the server send an ACK

1. Persistent asynchronous communication
2. Persistent synchronous communication
3. Transient asynchronous communication
4. Receipt-based transient synchronous communication
5. Delivery-based transient synchronous communication at message delivery: when the server start to process the message send an ACK
6. Response-based transient synchronous communication: when the server finish to process the message send an ACK
 
### Communication middleware

**Message Oriented Communication**

- Transient Communication: Berkeley sockets

|Primitive|Meaning|
|-|-|
|Socket|Create a new communication endpoint|
|Bind|Attach a local address to a socket|
|Listen|Announce willingness to accept connections|
|Accept|Block caller until a connection request arrives|
|Connect|Actively attempt to establish a connection|
|Send|Send some data over the connection|
|Receive|Receive some data over the connection|
|Close|Release the connection|

- Persistent Communication: Queuing Systems

    The relationship between queue-level addressing and network-level addressing.

- Message-queuing system with routers

When considering message queuing systems:

- When asynchronous communication is preferable
- When scalaility can be increased by admitting delays in requests and responses
- When the producer is faster than the consumer
- When implementing a publish-subscribe communication pattern

**Remote Procedure Call**

- Client procedure calls client stub in normal way
- Client stub builds message, calls local OS
- Client's OS sends message to remote OS
- Remote OS gives message to server stub
- Server stub unpacks parameters, calls server
- Server does work, returns result to the stub
- Server stub packs it in message, calls local OS
- Server's OS sends message to client's OS
- Client's OS gives message to client stub
- Stub unpacks result, returns to client

Marshalling and Unmarshalling:

- Parameter marshalling: the procedure to format RPC parameters in
a message
- Parameter unmarshalling: the inverse procedure of extracting the
parameters from the message
- Marshalling requires the serialization of objects.

Synchronous: 

- Client Call remote procedure 
- Server Call local procedure and return results to the client

Asynchronous:

- Client Call remote procedure 
- Server Call local procedure and return Accept request

## Synchronization problems in distributed systems 

### Physical Clocks

**Using GNSS** (Global Navigation Satellite System)

- GNSS satellites have atomic clocks onboard
- GNSS satellites broadcast messages that include timing information
- GNSS receivers listen to multiple satellites and use trilateration to determine their own position and UTC time deviation

**Cristian’s algorithm and Network Time Protocol**

Ask the server what time it is and the client subtract the time the server answered me.

**The Berkeley Algorithm** (Internal synchronization)

It is not always necessary to align the DS node clocks with external physical clocks!

1. The time daemon asks all the other machines for their clock values.
2. The machines answer.
3. The time daemon tells everyone how to adjust their clock.

### Logical Clocks (Lamport)

In many cases it is not necessary that nodes agree on their physical clocks value

- if a --> b holds, then C(a) < C(b) should hold
- If a and b occur in the same process the goal is naturally achieved
- If a is the event of sending a message m by a node and b is the event of receiving m, then a --> b holds. How to ensure C(a) < C(b)?

**Lamport**

Updating counter Ci for process Pi

1. Before executing an event, Pi executes Ci <-  Ci + 1
2. When process Pi sends a message m to Pj, it sets m’s timestamp ts(m) equal to Ci
3. When Pj receives message m at Cj, adjusts its own local counter as: Cj <- max(Cj , ts(m)) + 1

**Lamport Total Order**

- The algorithm can be modified by attaching a process number to the timestamp of an event
- Pi timestamps event e with Ci(e).i where i is the process number
- For any two timestamps T1=(Ci(a),i) and T2=(Cj(b),j):
    - If Ci(a) < Cj(b) then T1 < T2
    - If Ci(a) > Cj(b) then T2 < T1
    - If Ci(a) = Cj(b) and i < j then T1 < T2
    - If Ci(a) = Cj(b) and i > j then T1 > T2

**Totally-Ordered Multicasting**

Assumpion, no messages are lost

Assumpion, nessagges from the same sender are received in the order they were sent

- Process Pi sends timestamped message mi to all others. The
message itself is put in a local queue i
- Any incoming message at Pj is queued in queue j, according to its timestamp, and ACKed to every other process (send and receive events for messages and acks are totally ordered with Lamport)
- Pj passes a message mi to its application if
    - mi is at the head of queue j AND
    - mi has been ACKed by each of the other processes

## Mutual exclusion

### A centralized algorithm

1. Process 1 asks the coordinator to access the resource. Access is granted. Then, process 2 asks for access. The coordinator does not answer, but adds the request to the queue.
2. When process 1 is done it notifies the coordinator that grants access to the first process in the queue in FIFO order.

Problems:

- Single point of failure for the crash of the coordinator
- Performance bottleneck
- Difficult to distinguish a problem of the coordinator process from the unavailability of the resource

### A distributed algorithm

Assumption: total order of events and reliable message delivery (ack system)

**Implementation** (Ricart and Agrawala)

1. If a process P wants to use a resource R it builds a message containing:
    - the name of RP
    - the ID of P
    - the current timestamp
    and sends the message to all the processes (including itself)

2. When a process Q receives a message we have 3 cases:
    - If Q is not using R and it does not require R, it answers OK to P
    - If Q is using R it does not answer and it queues the request
    - If Q wants to use R but it did not yet, it compares the message timestamp with the one in the message it sent out with its own request. The earliest wins. If the one in the message sent by P is lower it answers OK to P, otherwise it queues the message.

3. After sending out its message process P waits for OK from all processes before accessing R.

4. When P is done with R it sends OK to all processes in its queue and empties the queue.

Problems:

- No answer from a process may also be due to its crash
- Involving all processes of a distributed system may be a waste of resources

### A ring algorithm

1. Unordered group of processes
2. A software defined logic ring.

**Implementation**

1. At start, the token is given to process 0.
2. The token is sent with a message from process i to process (i+1)MOD n.
3. If a process is interested in the resource, it can access when it receives the token. When done it sends the token to the next process in the ring. It cannot use twice the same token.

## Election algorithms

- Electing a coordinator process may be useful
- Election algorithms aim at electing the active process with the highest identifier
- Some algorithms assume that each process knows the IDs and can communicate with any other process.

### Bully algorithm

1. A process contacts the old coordinator; it understands that it is not active anymore and starts an election by sending a message to all processes with an ID greater than their own.
2. The receivers answer telling that they will take care
3. The receivers start an election
4. The highest process send to all others that it will take care of the election, because it does not receives at least one ACK.  
5. The highest wins and tells everybody.

### A ring-based election (Chang and Roberts)

Assumptions: 

- N processes are logically ordered in a ring.
- Messages circulate clockwise in the ring without failures
- Processes have unique IDs

1. All processes are marked as non-participant
2. When a process Pk understands that the coordinator is not answering, it starts an election by marking itself as participant and sending to the next node in the ring a message <Election, ID(Pk)>
3. When a process Pm receives <ELECTION, ID(Pk)>
    - if ID(Pk) > ID(Pm) Pm forwards the message in the ring and marks itself as participant
    - if ID(Pk) < ID(Pm) if Pm is non-participant it changes to participant and forwards <Election, ID(Pm)>. If it is already participant it does not forward the message
    - If k=m (the received ID is its own) then it is the coordinator: it marks itself as non-participant and sends <ELECTED, ID(Pm)> to the next process
4. When a process Pk receives <ELECTED, ID(Pm)>
    - it marks itself as non-participant, stores the ID of the coordinator, and unless k=m it forwards the message to the next process

**Handling Failures**: Failures due to crash of nodes in the ring are handled by each process by storing, not only the address of the next process, but also a few others following it in the ring. If the communication with the next process fails, the message is sent to the first among the ones following it that is active.

**Concurrent elections**: The use of the participant/non-participant state helps extinguishing as soon as possible unneeded messages in concurrent elections.

## Fault Tolerance and Consensus

Being fault tolerant is strongly related to what are called dependable systems

Dependability implies the following:
1. Availability. The probability that the system operates correctly at any given moment
2. Reliability. The ability to run correctly for a long interval of time
3. Safety. Failure to operate correctly does not lead to catastrophic failures
4. Maintainability. The ability to “easily” repair a failed system

|Type of failure|Description|
|-|-|
|Crash failure|A server halts, but is working  correctly until it halts|
|Omission failure|A server fails to respond to incoming requests|
|Timing failure|A server's responnses lies outside the specified time interval|
|Response failure|A server's response is incorrect|
|Arbitrary failure|A server may produce arbitrary responses at arbitrary times|

Failure Masking by Redundancy:

- Information redundancy
- Time redundancy
- Physical redundancy

How much redundancy?

- If faulty processes just stop working (crash failure), k+1 processes provide k-fault tolerance
- If faulty processes reply with wrong values, at least 2k+1 processes are needed
- If a consensus in the group is needed the problem is harder and proved to be impossible in some cases

**Byzantine agreement with synchronous systems**

At least N=3k+1 processes are needed for k faulty processes

Example of solution for Byzantine generals problem for N=4 and k=1:

- the commander sends a value to each of the lieutenants
- each of the lieutenants sends the value it received to its peers (more rounds are needed for N>4)
- A lieutenant receives a value from the commander, plus N – 2 values from its peers. If the commander is faulty, then all the lieutenants are non-faulty and each will have gathered exactly the set of values that the commander sent out. Otherwise, one of the lieutenants is faulty; each of its correct peers receives N – 2 copies of the value that the commander sent, plus a value that the faulty lieutenant sent to it. In either case, the correct lieutenants need only apply a simple majority function to the set of values they receive. When no majority exists a special value is used.

**Synchronous versus asynchronous systems**:

- Synchronous systems:
    - Execution on each node is bounded in speed and time
    - Communication links have bounded transmission delay
    - Clock on each node has a bounded drift
- Asynchronous systems
    - Execution on each node can occur at arbitrary speed 
    - Communication links have different and unbounded transmission delay
    - Clock on each node has an unbounded drift

- Internet-based heterogeneous distributed systems are inherently asynchronous
- Coordination and agreement in asynchronous systems is hard and often impossible. We often make (partial) synchronicity assumptions
- In order to cooperate in reaching a common goal we need algorithms that achieve a form of synchronization

- FLP Theorem (1985). When delays in answering messages are arbitrary there is no guaranteed solution to Byzantine agreement (consensus in presence of Byzantine faults) neither to totally ordered multicast, even if a single node fails.
- There are solutions for partially synchronous systems that can be used to model practical systems.

**CAP** (for asynchronous systems)

- Consistency: Every read receives the most recent write or an error
- Availability: Every request reveives a response
- Partition tolerance: The system tolerates an arbitrary number of messages lost

**Practical consensus: the Paxos protocol**

- Goal: solving consensus in a network of unreliable or fallible processors ensuring consistency
- the basic version does not cover Byzantine failures. It tolerates k failing nodes with N=2k+1

**Practical consensus: the Raft protocol**

- same goal: a solution to state machine distribution preserving safety (consistency)
- based on leader election and log replication 
- it does not cover Byzantine failures
- It tolerates k failing nodes with N=2k+1

## Distributed Ledger Technologies and Blockchain

**The DLT System Model**

A distributed system with
- decentralized control
- nodes run by different entities that do not trust each other and may even be malicious (byzantine behavior)
- a copy of data records is stored at each node

A consensus problem:
- Nodes need to agree on a history of data

**The Blockchain approach**

- Each transaction is digitally signed (with private key of the sender) and propagated to all participating nodes
- When a node receives a transaction, it validates it
- Validated transactions are still considered "pending" as they are not  yet part of the chain
- In a blockchain, transactions are grouped in timestamped blocks and the whole history is stored at each node as a chain of blocks

**Consensus in blockchain**

The challenge is for the nodes to have a consensus on the blocks and on the sequence of blocks

Main idea:

- compute the hash of each transaction, and of a Block
- compute the hash of a block including the hash of the previous block in the chain
- including a trick to make the computation of the block hash expensive but very easy to verify
- make the nodes compete on this computation with a reward, and have th e winner propagate its computed block to the others

**Blockchain PoW algorithm**

- The algorithm used for consensus is called Proof-Of-Work (PoW)
- Verifying a block requires solving a computational puzzle while computing its hash
- A miner node needs to find a number (nonce) such that the hash of the block has particular property
- Solving the puzzle requires a brute force approach
- A reward is given to miners that win
- A veri ed block is sent to all nodes
- When a node receives a block, it checks the puzzle solution and then adds it to its local copy of the chain

**Blockchain properties**

- Assuming most nodes are working on the same chain, the one growing fastest will be the longest and most trustworthy
- In order for a malicious node to change a transaction in an intermediate block, it has to re-compute all the subsequent block hashes and prevail over other nodes in the network
- Blockchain is safe as long as more than 50% of the work being put in by miners is honest.

**Smart contracts**

- The Blockchain is useful to store more than nancial transactions. Ethereum was speci cally designed for smart contracts and more.
- Smart contract: A piece of software code defining a self-executing “contract”. While originally proposed as digital version of a legal contract it can be a general software program.
- Each node can verify if the conditions of the contract are satis ed and perform the consequent actions. In the end all nodes should agree on the resulting “state”.

## Introduction to Pervasive Computing

**Mobile computing**

Main issues:
- limited resources (energy, CPU, memory, ...)
- different types of interfaces
- high variance in connectivity
- variable location

**IoT** (Internet of things)

- Device IoP (Internet of People): devices that let people access the system, such as smartphones.
- Device IoT with IP: devices that can access the Internet network and send data.
- Device without IP: usually used in IoT context, but that can not access the Internet network.

**Pervasive computing**

New issues;
- smart spaces need to be effectively used
- invisibility: interaction with users should be minimized
- resources in a pervasive environment should be discoverable and dynamic association/collaboration should be enabled

## Distributed and pervasive systems

**Introduction to sensor and sensor devices**

Transducer: device that transforms one from energy into another. 

Input transducers: sensors. 

Output transducers: actuators.

**Main types of sensors**

Physical sensors:

- Motion sensors: They measure acceleration forces and rotational forces along three axes.
- Environmental sensors: They measure environmental parameters, such as ambient air temperature and pressure, illumination, and humidity
- Position sensors. They measure the physical position of a device. This category includes orientation sensors and magnetometers.

Virtual sensors:
- Services and apps that provide context data to remote clients.

**Actuators**

Actuators are also a particular type of transducers and they are usually powered and they convert energy into an action. 

Home: Zigbee ~ Z-Wave -> Bluetooth -> WiFi

World: Thread -> ESP WiFi -> 5g -> LoRaWAN

**Matter**

- A standard for smart-home device connectivity
- Focused on security, easy-of-use, reliability
- Designed to run on any network stacks that support IP. In the Matter 1st release, it supports WiFi, Thread, and Ethernet protocols.

**Managing and querying sensor data**

Different problem w.r.t. traditional databases.

- Continuous vs one-time
- Strong spatio-temporal characterization of data

### Basic methods

Batch processing 

- Buffering on the sensor, and offline processing on the base station
- Precise answer; no processing on the sensor; but high communication costs
- The base station receives all the data (but with a delay)

Sampling

- Not all the sensed signal is used
- Statistics obtained through sensor readings extracted according to a given probability distribution
- Provides formal guarantees about the introduced error

Sliding windows

- Approximate answer based on a group of consecutive readings
- Run-time computation on the device
- The base station receives a continuous stream of approximated sensor readings

### Advanced methods

In-network query processing

- (opposed to centralized processing)
- build an overlay network
- perform data aggregation in intermediate nodes to reduce transmission 

Duty cycling

- The radio is put on sleep mode most of the time
- Coordinated sleep/wakeup scheduling algorithm

Mobility-based

- The base station may be mobile
- Nodes may be carried by people, cars
- Exploit mobility to better distribute the transmission cost between nodes

### Model-based approaches

- Sampled data may have strong spatio-temporal correlation
- Objective: reduce the number of samples while keeping good data quality
- Method: exploiting the model of the underlying phenomena 

**Approaches**

Data cleaning: identifying noisy readings

Data acquisition: efficiently acquiring samples from the sensors

Query processing: processing queries by accessing or generating minimal amount of data 

Data compression: eliminating redundancy

### Data cleaning

**Sensor data cleaning**

Sensor data are uncertain and erroneous
- discharged batteries, network failures
- low-quality sensors, freezing/heating of the casing or measurement device
- accumulation of dirt, mechanical failure or vandalism

Model-based data cleaning
- the most probable sensor values are inferred using statistical models
- anomalies are detected by comparing raw sensor values with the
corresponding inferred sensor values

polynomial regression models can capture both continuity and correlation

### Data acquisistion

**Pull-based data acquisition**

The user defines the interval and frequency of data acquisition

**Push-based data acquisition**

- The sink and the sensors agree on an expected behavior of the sensor values
- If sensed values deviate from the model, the sensors communicate only the unexpected values

Types of models:
- Probabilistic models: Linear prediction
- Markovian models: Consider complex dependencies among sensors

### Model-based compression

- Sensor may produce high volumes of data
- Approximate a sensor data stream by a set of functions
- Regression, transformation and filtering can be used to approximate sensor data streams exploiting spatio-temporal correlations
- Orthogonal transformation methods reduce the data dimensionality

## Context awareness

- Traditional software applications cannot understand the “context” of a request

**Temporal context**

Context history plays an important role
- keeping track of context data enables
    - deriving new context (e.g., by knowing a sequence of positions we can obtain a trajectory)
    - predicting context (e.g., observing a recurrent trajectory at a given time we can predict current destination)

**Adaptiveness**

- The property of a system to adapt to a given context for providing a better service/experience
- A context-aware system acquires context data to automatically adapt its behavior
- Very important for mobile computing because of:
    - changes in network connectivity 
    - changes in energy availability 
    - limited interfaces to specify parameters
    - changes in user situation
    - changes in environment

Types of adaptiveness:
- Adapting functionality: the system may change the data flow
- Adapting data: the system may provide less or more precise position data

**Obtaining context data**

Low-level context:

Directly acquired from sensors or other sources

Obtained by simple processing and/or fusion of raw data

**Inferring context data**

High-level context:

Derived by applying inference methods on low level context.

Inference can also be obtained by reasoning on high-level context and common knowledge

Inference methods:

- Symbolic approaches: horn logic programs, general logic programs, description logics.
- Statistical approaches: classification, clustering

Context representation: where do you use these data? We need a common representation language -> a formal representation of data is needed to automatically process them


The representations for storing context are:
- Key/value pairs (flat)
- Markup languages (flat): more accurate with structures and hierarchies 
- Entity/Relationships (DB approach): they came up with a language called CML (is not a standard).
- Ontological models: described in terms of classes and relationships. Underneath there is formalies of mathematical logics that allow reasoning→ describing a situation semantically: We gain support for automatic reasoning 















