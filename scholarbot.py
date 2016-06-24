from flask import Flask, jsonify, request
from crossrefquery import CrossRef
from journaltocquery import JournalTOC
import operator

app = Flask(__name__)

@app.route('/v1')
def version1():
    date = (request.args.get('date'))
    words = request.args.get('words')
    z = []
    toc = JournalTOC().getjournaltoc(words)
    z.extend(toc)
    # dropping crossref for now bc journaltoc is too slow but is more recent results
    # stuff = ['book', 'monograph']
    # for s in stuff:
    #     res = CrossRef().getcrossref(s, date, words)
    #     z.extend(res)
    z.sort(key=operator.itemgetter('date'), reverse=True)
    foo = z[:30]
    length = len(foo)
    return jsonify({'length': length, 'results': foo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
    #app.run(debug = True)
