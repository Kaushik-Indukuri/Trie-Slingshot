# Server Documentation
## How the server is hosted
The server is hosted to AWS using the EC2 service. It's hosted on a t2.large instance of an ubuntu server. 
I connected to the instance by using SSH with the public IP address and the private key pair. 
Once connected, I downloaded all my required packages in Ubuntu. 
I created a new project directory and used SCP (secure copy) to transfer the server.py and trie.py files to the directory.
Finally I ran the server using gunicorn and allowed 3 workers so 3 clients can concurrently use the CLI. 
The order of requested operations across the clients was handled by making the workers synchronous. 
This forces the workers to handle only one request at a time, so they will be processed one after another. 
Then, I just changed the CLI from the local IP to the IP of the instance. 


## CLI interaction with the server
The CLI interacts with the server using HTTP GET and POST requests with the public IP of the instance mentioned above. For the add and delete commands, POST requests are used, and for the search, autocomplete, and display commands, GET requests are used. The server returns a JSON string which is then read and displayed 
on the command line.  


## Restful APIs 
- add: adds a word to the trie
- delete: deletes word from the trie
- search: searches whether a word is in the trie or not
- autocomplete: returns a list of autocomplete suggestions based on an input prefix
- display: displays all words in the trie
All the logic can be found at `./trie/services/server.py`
