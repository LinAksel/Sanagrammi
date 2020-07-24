from flask import Flask, jsonify, request
from src.words import sample_words, check_anagram

app = Flask(__name__)

@app.route('/')
def funktio():
    return 'Hello, World!'

@app.route('/reader')
def reader():
    return jsonify(sample_words(1))

@app.route('/check', methods = ['POST'])
def check():
    words = request.json
    correct = check_anagram(words['word'], words['candidate'])
    return jsonify({ 'correct': correct })

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Headers'] = 'Content-Type'
    header['Access-Control-Allow-Origin'] = '*'
    return response