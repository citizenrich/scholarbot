# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from crossrefquery import *
import json

#test
# stuff = 'book' #book, dissertation, monograph, journal-article, book-chapter
# test = ['Cold War']
# z = requestarticles(stuff, test)
# print z

app = Flask(__name__)

@app.route('/v1') #http://127.0.0.1:5000/v1?words=Stalin
def hello_world():
    cat = (request.args.get('cat'))
    words = [request.args.get('words')]
    resp = requestarticles(cat, words)
    length = len(resp)
    return jsonify(length = length)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
    #app.run(debug = True)
