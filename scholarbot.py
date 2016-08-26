from flask import Flask, jsonify, request
from providers.crossrefquery import CrossRef
from providers.journaltocquery import JournalTOC
import operator

app = Flask(__name__)

@app.route('/v1')
def version1():
    date = (request.args.get('date'))
    words = request.args.get('words')
    z = []
    toc = JournalTOC(words)
    toc_res = toc.getjournaltoc()
    z.extend(toc_res)
    if z <= 2:
        res = CrossRef('journal-article', date, words)
        res_res = res.getcrossref()
        z.extend(res_res)
    z.sort(key=operator.itemgetter('date'), reverse=True)
    foo = z[:10]
    length = len(foo)
    return jsonify({'length': length, 'results': foo})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)
