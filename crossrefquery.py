from habanero import Crossref
import requests
import json

"""
crossref api queries return authors and journal titles from the keywords, so restrict to just title
"""

def requestarticles(cat, keywords):
    results = []
    url = 'http://api.crossref.org/works?'
    payload = {'query': keywords, 'filter': 'type:{bdmj},from-pub-date:2013-01'.format(bdmj = cat), 'rows': 20} #20 max
    x = requests.get(url, params=payload)
    xdict = x.json()
    for i in xdict.get('message').get('items'):
        url = i.get('URL')
        title = i.get('title')[0]
        try:
            container = i.get('container-title')[0]
        except:
            container = ''
        try:
            firstauthor = i.get('author')[0].get('family')
        except:
            firstauthor = ''
        result = {'firstauthor': firstauthor, 'title': title, 'container': container, 'url': url, 'intitle': []}
        results.append(result)
    for idx, val in enumerate(results):
        x = [i for i in keywords if i in val.get('title')]
        val['intitle'] = x
    results[:] = [el for el in results if el.get('intitle')]
    return results

#tests
# stuff = 'book' #book, dissertation, monograph, journal-article, book-chapter
# test = [u'Nixon', u'Cold War']
# z = requestarticles(stuff, test)
# print z

def crossrefarticles(cat, keywords):
    results = []
    cr = Crossref()
    x = cr.works(query = keywords, filter = {'from-pub-date': '2013-01', 'type': cat}, limit = 20) #sort = 'published' drops things
    for i in x['message']['items']:
        url = i['URL']
        title = i['title'][0]
        try:
            container = i['container-title'][0]
        except:
            container = ''
        try:
            firstauthor = i['author'][0]['family']
        except:
            firstauthor = ''
        result = {'firstauthor': firstauthor, 'title': title, 'container': container, 'url': url, 'intitle': []}
        results.append(result)
    for idx, val in enumerate(results):
        x = [i for i in keywords if i in val.get('title')]
        val['intitle'] = x
    results[:] = [el for el in results if el.get('intitle')]
    return results

#tests
# stuff = 'book' #book, dissertation, monograph, journal-article, book-chapter
# test = [u'Nixon', u'Cold War']
# z = crossrefarticles(stuff, test)
# print z

#grab below for years if necessary
# u 'published-print': {
#     u 'date-parts': [
#         [2015, 10, 5]
#     ]
