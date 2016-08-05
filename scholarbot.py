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
    # this deals with journaltoc outage
    if not z:
        res = CrossRef().getcrossref('journal-article', date, words)
        z.extend(res)
    # not using books for now
    # if not z:
    #     stuff = ['book', 'monograph']
    #     for s in stuff:
    #         res2 = CrossRef().getcrossref(s, date, words)
    #         z.extend(res2)
    z.sort(key=operator.itemgetter('date'), reverse=True)
    foo = z[:10]
    length = len(foo)
    return jsonify({'length': length, 'results': foo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
    #app.run(debug = True)
