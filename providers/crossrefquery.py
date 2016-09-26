import requests
import json
# import urllib


class CrossRef(object):
    """
    bdmj: book, dissertation, monograph, journal-article, book-chapter
    20 queries max in one go
    """
    def __init__(self, cat, since, keywords):
        self.cat = cat
        self.since = since
        self.keywords = keywords
        self.results = []
        self.base = 'http://api.crossref.org/works?'
        self.limit = 10
        self.url = ''

    def getcrossref(self):
        # addurl = urllib.pathname2url(keywords) #alternative approach to building query.
        payload = {
                    'query.title': self.keywords,
                    'filter': 'type:{bdmj},from-pub-date:{date}'.format(bdmj=self.cat, date=self.since),
                    'rows': self.limit
                }

        # payload = {
        #             'query.title': '\"{key}\"'.format(key = addurl),
        #             'filter': 'type:{bdmj},from-pub-date:{date}'.format(bdmj=cat, date=since),
        #             'rows': 20
        #         }
        x = requests.get(self.base, params=payload)
        self.url = x.url
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
            result = {
                        'type': typeof,
                        'date': date,
                        'title': title,
                        'url': url,
                        'source': 'crossref'
                    }  # fulltitle for title issue
            if self.keywords.lower() not in result.get('title').lower():
                continue
            else:
                self.results.append(result)
        return self.results

# tests
# stuff = 'journal-article'
# when = '2015-01'
# test = 'cold war'
# z = CrossRef(stuff, when, test)
# print z.getcrossref()
# print z.url
