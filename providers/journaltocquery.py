import feedparser
import requests

class JournalTOC(object):
    """
    no category - journal articles only, to= is limit, max is 300; no timeframe - just the most recent
    """
    def __init__(self,keywords):
        self.keywords = keywords
        self.results = []
        self.base = 'http://www.journaltocs.ac.uk/api/articles/'
        self.limit = 10

    def getjournaltoc(self):
        params = {'to': self.limit}
        url0 = '%s%s' % (self.base, self.keywords)
        response = requests.get(url0, params=params)
        self.url = response.url
        rssdoc = feedparser.parse(response.content)
        for i in rssdoc.get('entries'):
            url = i.get('link')
            title = i.get('title')
            if str(i.get('date')) == 'None':
                dateall = ''
            else:
                dateall = str(i.get('date'))
            date = dateall[:10]
            result = {'type': 'journal-article',
                        'date': date,
                        'title': title,
                        'url': url,
                        'source': 'journaltoc'}
            if self.keywords.lower() not in result.get('title').lower():
                continue
            else:
                self.results.append(result)
        return self.results

#tests
# test = 'Neural networks'
# z = JournalTOC(test)
# print z.getjournaltoc()
# print z.url, z.keywords
