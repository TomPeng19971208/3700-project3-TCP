TCP Protocol Implementation
This is a customized TCP implementation using UDP socket. We aims to create a reliable transfer protocol similar to a real TCP protocol.
The sender can send a number of packets eqauls to the current sliding window size, store a copy of each packet, and then listen for ACK.
Each time an ACK is received, corresponding packet will be removed from the copy. Next round of sending starts when all ACK for packets
sent in the first round are received (when the copy at sender side becomes empty). If the socket times out, the program will retransmit
all of the unacked packets. Sender's window size and socket's timeout are reset after each round. 

Chalenges and Solution:
1) avoid congestion and adjust sender's window  
Initially, sender's window size is set to 1. Everytime a ACK of any packet that has not been retranmitted is received, window size will
be multiplied by 2. This will continue until it reaches the threshold. After the threshold is reached, window size will be incremented or
set to threshold/2 depends on whether the sender can still receive correct ACKs. 
2) adjust socket's timeout
The program distinguishes dropped packets and delayed packets by examing how many times the packet has been retransmitted. Each ACK contains
an integer field to record times of retranmition of that packet. By comparing that number with sender's record, we can determin if that data chunk
1) has been transmitted successfully 2) is delayed and retransmitted 3) is dropped and retransmitted. Every time we send a packet and receive its ack, 
we will record the RTT. Socket timeout is set to RTT in case 1, 2xTIMEOUT in case 2, and 0.5 * TIMEOUT in case 3. 

Test:
We use the test program provided by the professor to test our protocol. This protocol is tested under conditions with various packet delay, 
drop rate, reorder rate, and bandwidth.  
