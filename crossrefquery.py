import requests
import json
import urllib

class CrossRef(object):
    """
    bdmj: book, dissertation, monograph, journal-article, book-chapter, 20 queries max in one go
    """

    def getcrossref(self, cat, since, keywords):
        results = []
        url = 'http://api.crossref.org/works?'
        #addurl = urllib.pathname2url(keywords)
        payload = {'query.title': keywords, 'filter': 'type:{bdmj},from-pub-date:{date}'.format(bdmj = cat, date = since), 'rows': 20}
        #payload = {'query.title': '\"{key}\"'.format(key = addurl), 'filter': 'type:{bdmj},from-pub-date:{date}'.format(bdmj = cat, date = since), 'rows': 20}
        x = requests.get(url, params=payload)
        xdict = x.json()
        for i in xdict.get('message').get('items'):
            url = i.get('URL')
            title = i.get('title')[0]
            # for books, but not really needed otherwise
            # try:
            #     subtitle  = i.get('subtitle')[0]
            #     fulltitle = title + ': ' + subtitle
            # except:
            #     fulltitle = title
            dateall = str(i.get('deposited').get('date-time'))
            date = dateall[:10]
            typeof = i.get('type')
            result = {'type': typeof, 'date': date, 'title': title, 'url': url, 'source': 'crossref'} #fulltitle for title issue
            if keywords.lower() not in result.get('title').lower():
                continue
            else:
                results.append(result)
        return results

#tests
# stuff = 'book'
# when = '2015-01'
# test = 'cold war'
# z = CrossRef().getcrossref(stuff, when, test)
# print z
