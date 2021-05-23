/*0
--------{GRN} CHATNET PROTOCOL IMPLEMENTATION {}--------
{CYN}Description{} Secure communication under the Chatnet 
            protocol without using database.
{CYN}Repository{}  http://github.com/midnqp/chatnet
{CYN}License{}     MIT

This C program creates p_threads to receive messages and 
incoming connection requests. Also, send messages.

All required header files:
*/

#include "libcpyb.h"    
#include "libchatnet.h" 
#include <ncurses.h>
#include <form.h>
/*4 
libcpyb.h    - contains stdio, stdlib, etc
libchatnet.h - core client implementation
ncurses.h    - input message to be sent
form.h       - helps to ncurses


*/


void* print_received_msg(void* arg) {
	//0 {GRNBG}Section{} Displaying received messages
	//4 Takes (void*)NULL argument
  ...
}

void* print_incoming_conn_req(void* uSend, void* shkey) {
	//0 {GRNBG}Section{} Displaying incoming connection requests
	//4 Requires username of sender
	//4 Requires cryptographic shared key
	...
}
