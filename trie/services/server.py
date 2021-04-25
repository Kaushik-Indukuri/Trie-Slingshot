from flask import Flask, request, jsonify
from trie import Trie
import json

__author__ = "Kaushik"

app = Flask(__name__)
t = Trie()
in_trie = False


def query():
    args = request.args
    if "word" in args:
        word = args.get("word")
    if not word:
        flask.abort(404)
    word = word.strip()
    global in_trie
    in_trie = t.search(word)
    return word


@app.route('/')
def home():
    return '<h1>Trie Project</h1>'


@app.route('/add', methods=["POST"])
def add():
    word = query()
    if in_trie:
        return flask.jsonify({"output": word + " is already in the trie"})
    elif not in_trie:
        t.add(word)
        return flask.jsonify({"output": word + " has been added"})
    else:
        raise ValueError("Error, try again")


@app.route('/delete', methods=["POST"])
def delete():
    word = query()
    if in_trie:
        t.delete(word)
        return flask.jsonify({"output": word + " has been deleted"})
    elif not in_trie:
        return flask.jsonify({"output": word + " is not in the trie"})
    else:
        raise ValueError("Error, try again")


@app.route('/search', methods=["GET"])
def search():
    word = query()
    if in_trie:
        return flask.jsonify({"output": word + " was found in the trie"})
    elif not in_trie:
        return flask.jsonify({"output": word + " was not found in the trie"})
    else:
        raise ValueError("Error, try again")


@app.route('/autocomplete', methods=["GET"])
def autocomplete():
    word = query()
    response = t.autocomplete(word)
    if response is None:
        return flask.jsonify({"output": "No autocomplete suggestions"})
    elif response is not None:
        return flask.jsonify({"output": "Autocomplete suggestions for " + word + ": {}".format(response)})
    else:
        raise ValueError("Error, try again")


@app.route('/display', methods=["GET"])
def display():
    if len(t.display()) == 0:
        return flask.jsonify({"output": "Trie is empty"})
    elif len(t.display()) >= 1:
        response = t.display()
        return flask.jsonify({"output": "Trie: {}".format(response)})
    else:
        raise ValueError("Error, try again")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
