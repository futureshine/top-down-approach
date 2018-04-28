### UDP Pinger

In this programming assignment, you will write a client ping program in Python.
Your client will send a simple ping message to a server, receive a corresponding
pong message back from the server, and determine the delay between when the
client sent the ping message and received the pong message. This delay is called the
Round Trip Time (RTT). The functionality provided by the client and server is similar 
to the functionality provided by standard ping program available in modern
operating systems. However, standard ping programs use the Internet Control Message Protocol (ICMP) (which we will study in Chapter 4). Here we will create a
nonstandard (but simple!) UDP-based ping program.

Your ping program is to send 10 ping messages to the target server over UDP.
For each message, your client is to determine and print the RTT when the corresponding pong message is returned. Because UDP is an unreliable protocol, a packet sent
by the client or server may be lost. For this reason, the client cannot wait indefinitely
for a reply to a ping message. You should have the client wait up to one second for a
reply from the server; if no reply is received, the client should assume that the
packet was lost and print a message accordingly.


### Usage
open two terminals in your machine, run server.py in one and run client.py in the other.
