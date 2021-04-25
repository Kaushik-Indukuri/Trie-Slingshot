# Slingshot Trie Project 
Contributors: Kaushik Indukuri



## Installing CLI
Clone this repo and navigate to the project directory
```
# At project directory 
pip install --editable . 
```
You are done installing.
Get started by typing trie 


## Interacting with CLI
Format for commands:
trie -w TEXT COMMAND
```
trie -w hi add
trie -w hi delete
trie -w hi search 
trie -w hi autocomplete 
trie display
```


## Example Test Suite
### Blank
```
trie -w add
# Expect a missing command error
```
### Add
```
trie -w hello add
# Expect "hello has been added"
trie -w hello add
# Expect "hello is already in the trie"
```
### Search
```
trie -w hello search
# Expect "hello was found in the trie"
trie -w nice add
# Expect "nice was not found in the trie"
```
### Autocomplete
```
trie -w hel autocomplete
# Expect "Autocomplete suggestions for hel: ['hello']"
trie -w sho autocomplete
# Expect "No autocomplete suggestions"
```
### Delete and Display
```
trie display
# Expect "Trie: ['hello']"
trie -w hello delete
# Expect "hello has been deleted"
trie -w bro delete
# Expect "bro is not in the trie"
trie display
# Expect "Trie is empty"
```


## Debugging
Test locally to debug
```
gunicorn --workers=3 --bind 0.0.0.0:8080 server:app -D
# To start server
trie -s http://0.0.0.0:8080 -w good add
# -s allows user to manually change ip
# Insead of using the global server ip, you can overide to the local server ip you ran above with gunicorn
```


## TODO
Make server more scalable since only 3 workers can currrently run at the same time

Improve efficiency of trie 
