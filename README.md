# `codebase-autodoc`
![](https://raw.githubusercontent.com/midnqp/midnqp/main/cdn/autodoc1.png)
- provided an __extremely simple format__ for writing documentation, inside source code
- view/output __scattered documentation texts__ from inside of source code
- flexible enough to view __all/most documentation format__


## Example
```C
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
  //0 \n\n\n
  //0 {GRNBG}Section{} Displaying received messages
  //4 Takes (void*)NULL argument
  ...
}

void* print_incoming_conn_req(void* uSend, void* shkey) {
  //0 \n
  //0 {GRNBG}Section{} Displaying incoming connection requests
  //4 Requires username of sender
  //4 Requires cryptographic shared key
  ...
}
```
