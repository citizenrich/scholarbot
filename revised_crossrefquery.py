import requests
import json

"""
bdmj: book, dissertation, monograph, journal-article, book-chapter
20 queries max in one go
crossref api queries return authors and journal titles from the keywords, so restrict to just title
"""

def requestarticles(cat, keywords):
    results = []
    url = 'http://api.crossref.org/works?'
    payload = {'query': keywords, 'filter': 'type:{bdmj},from-pub-date:2013-01'.format(bdmj = cat), 'rows': 20}
    x = requests.get(url, params=payload)
    print x.url
    print cat
    print keywords
    xdict = x.json()
    for i in xdict.get('message').get('items'):
        url = i.get('URL')
        title = i.get('title')[0]
        result = {'title': title, 'url': url, 'intitle': []}
        results.append(result)
    for idx, val in enumerate(results):
        x = [i for i in keywords if i.lower() in val.get('title').lower()]
        val['intitle'] = x
    output = [el for el in results if el.get('intitle')]
    return output

#tests
stuff = 'book'
test = [u'Nixon', u'cold war']
z = requestarticles(stuff, test)
#print z

#stuff = 'monograph'
#w = requestarticles(stuff, test)
#print w
#y = z + w
#print y[9]
