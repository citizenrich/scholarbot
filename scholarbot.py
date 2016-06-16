from flask import Flask, jsonify, request
from crossrefquery import *
from journaltocquery import *
import operator

app = Flask(__name__)

@app.route('/v1')
def version1():
    date = (request.args.get('date'))
    words = request.args.get('words')
    z = []
    toc = getjournaltoc(words)
    z.extend(toc)
    stuff = ['book', 'monograph', 'journal-article', 'book-chapter']
    for s in stuff:
        res = getcrossref(s, date, words)
        z.extend(res)
    z.sort(key=operator.itemgetter('date'), reverse=True)
    length = len(z)
    return jsonify({'length': length, 'results': z})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
    #app.run(debug = True)
