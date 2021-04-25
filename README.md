# Slingshot Trie Project 
Contributors: Kaushik Indukuri



## Installing CLI
Clone this repo and navigate to the project directory

On Windows:
```
# Activating virtual environment
venv\Scripts\activate.bat
```
On Mac and Linux:
```
# Activating virtual environment
source venv/bin/activate
```
Installing the CLI:
```
# At project directory
pip install --editable . 
```
You are done installing.
Get started by typing trie/cli.py


## Interacting with CLI
Format for commands:
trie/cli.py -w TEXT COMMAND
```
trie/cli.py -w hi add
trie/cli.py -w hi delete
trie/cli.py -w hi search 
trie/cli.py -w hi autocomplete 
trie/cli.py display
```


## Example Test Suite
### Blank
```
trie/cli.py -w add
# Expect a missing command error
```
### Add
```
trie/cli.py -w hello add
# Expect "hello has been added"
trie/cli.py -w hello add
# Expect "hello is already in the trie"
```
### Search
```
trie/cli.py -w hello search
# Expect "hello was found in the trie"
trie/cli.py -w nice add
# Expect "nice was not found in the trie"
```
### Autocomplete
```
trie/cli.py -w hel autocomplete
# Expect "Autocomplete suggestions for hel: ['hello']"
trie/cli.py -w sho autocomplete
# Expect "No autocomplete suggestions"
```
### Delete and Display
```
trie/cli.py display
# Expect "Trie: ['hello']"
trie/cli.py -w hello delete
# Expect "hello has been deleted"
trie/cli.py -w bro delete
# Expect "bro is not in the trie"
trie/cli.py display
# Expect "Trie is empty"
```


## Debugging
Test locally to debug
```
gunicorn --workers=3 --bind 0.0.0.0:8080 server:app -D
# To start server
trie/cli.py -s http://0.0.0.0:8080 -w good add
# -s allows user to manually change ip
# Insead of using the global server ip, you can overide to the local server ip you ran above with gunicorn
```


## TODO
- Make server more scalable by transitioning to asynchronous workers so requests won't get piled up
- Improve efficiency of trie 
