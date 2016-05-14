from flask import Flask, jsonify, request
from crossrefquery import *

app = Flask(__name__)

@app.route('/v1')
def hello_world():
    cat = (request.args.get('cat'))
    words = [request.args.get('words')]
    x = requestarticles(cat, words)
    return jsonify({'results': x})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
    #app.run(debug = True)
