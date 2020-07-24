from flask import Flask, jsonify
from random import sample
from xml.etree import ElementTree

app = Flask(__name__)

@app.route('/')
def funktio():
    return 'Hello, World!'

@app.route('/reader')
def reader():
    root = ElementTree.parse('sanalista.xml').getroot()
    words = []
    for element in root:
        word = element[0].text
        words.append(word)
    return jsonify(sample(words, 10))