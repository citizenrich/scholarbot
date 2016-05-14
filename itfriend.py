# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from crossrefquery import *
import json

app = Flask(__name__)

@app.route('/v1') #http://127.0.0.1:5000/v1?words=Stalin
def hello_world():
    cat = (request.args.get('cat'))
    words = [request.args.get('words')]
    output = requestarticles(cat, words)
    return jsonify({'results': output})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
    #app.run(debug = True)
