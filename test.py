myList = [{'url': u'http://dx.doi.org/10.4324/9781315733661', 'intitle': [u'Cold War'], 'title': u'Cold War Theatre (Routledge Revivals)'}, {'url': u'http://dx.doi.org/10.4324/9781315780962', 'intitle': [u'Cold War'], 'title': u'Thailand in the Cold War'}]


for i, title in enumerate(d for d in myList):
    print i,d.get('title')
