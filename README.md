
# `codebase-autodoc`
![](https://raw.githubusercontent.com/midnqp/midnqp/main/cdn/autodocReadme1.png)

- View __scattered documentation__ from inside of source code.




## USAGE
```C
/*0
--------{GRN} CHATNET PROTOCOL IMPLEMENTATION {}--------
{CYN}Description{} Secure communication under the Chatnet 
            protocol without using database.
{CYN}Repository{}  http://github.com/midnqp/chatnet
{CYN}License{}     MIT
This C program creates p_threads to receive messages and 
incoming connection requests, and to send messages.

All required header files:
*/
#include "midnqp/libcpyb.h"
#include "midnqp/chatnet/libchatnet.h" 
/*4 
libcpyb.h    - contains stdio, stdlib, etc
libchatnet.h - core client implementation
form.h       - input text of message/file/directory to send to friend

*/
void* print_received_msg(void* arg);
	//0 {GRNBG}Section{} Displaying received messages
	//4 Takes (void*)NULL argument
void* print_incoming_conn_req(void* uSend, void* shkey);
	//0 {GRNBG}Section{} Displaying incoming connection requests
	//4 Requires username of sender
	//4 Requires cryptographic shared key between uSend and uRecv(friend)
```
![](https://raw.githubusercontent.com/midnqp/midnqp/main/cdn/autodocReadme2.png)

## FORMAT
1. Tokens for _single-line `ts2`_ or _multi-line `ts`  `te`_ comments vary upon languages, and all are supported.

|Language|ts|te|ts2|
|--------|--|--|---|
|Javascript |   `/*`   |   `*/`   |   `//`  |
|Python     |   `'''`  |   `'''`  |   `#`   |
|CSS        |   `/*`   |   `*/`   |   `none`  |

2. To differentiate documentable comments, it's required to append an integer `indent` after `ts`.
```C
/*8
Multi-line comment started. Here indent is 8 spaces.
Multi-line comment
*/

//0 This is a single-line comment with indent set to 0 spaces.
```
3. Colors and text manipulations are supported.
	- `GRNBG` `REDBG` `BLU` `ULINE` `BOLD` etc. are for text manipulation and colors.

