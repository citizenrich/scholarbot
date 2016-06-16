import feedparser
import requests

def getjournaltoc(keywords):
    results = []
    base = 'http://www.journaltocs.ac.uk/api/articles/'
    params = ''
    url = '%s%s' % (base, keywords)
    response = requests.get(url, params=params)
    rssdoc = feedparser.parse(response.content)
    for i in rssdoc.get('entries'):
        url = i.get('link')
        title = i.get('title')
        if str(i.get('date')) == 'None':
            dateall = ''
        else:
            dateall = str(i.get('date'))
        date = dateall[:10]
        result = {'type': 'journal-article', 'date': date, 'title': title, 'url': url, 'source': 'journaltoc'}
        if keywords.lower() not in result.get('title').lower():
            continue
        else:
            results.append(result)
    return results

#tests
# test = 'putin'
# z = getjournaltoc(test)
# print z
