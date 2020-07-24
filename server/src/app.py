from flask import Flask, jsonify, request
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
    return jsonify(sample(words, 1))

@app.route('/check', methods = ['POST'])
def check():
    words = request.json
    return jsonify(words)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Headers'] = 'Content-Type'
    header['Access-Control-Allow-Origin'] = '*'
    return response