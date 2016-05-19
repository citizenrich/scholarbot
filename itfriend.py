from flask import Flask, jsonify, request
from crossrefquery import *

app = Flask(__name__)

@app.route('/v1')
def hello_world():
    cat = (request.args.get('cat'))
    words = [request.args.get('words')]
    if cat == 'book':
        bks = requestarticles(cat, words)
        cat = 'monograph'
        mono = requestarticles(cat, words)
        z = bks + mono
    z = requestarticles(cat, words)
    length = len(z)
    return jsonify({'length': length, 'results': z})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
    #app.run(debug = True)
