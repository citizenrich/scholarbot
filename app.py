# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request
from crossrefquery import *

stuff = 'book' #book, dissertation, monograph, journal-article, book-chapter
test = [u'Nixon', u'Cold War']
z = requestarticles(stuff, test)
print z

app = Flask(__name__)

@app.route('/v1') #http://127.0.0.1:5000/v1?words=Stalin
def hello_world():
    cat = (request.args.get('cat'))
    words = [request.args.get('words')]
    resp = requestarticles(cat, words)
    length = len(resp)
    return json.dumps({'length': length, 'results': resp})
    #return jsonify({'length': length, 'results': z})
    #fyi, textit.in can index arrays and do nested, e.g. @extra.products.0.name

if __name__ == '__main__':
    app.run(debug = True)
