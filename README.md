# ScholarBot
A simple web service to return links to the latest academic papers that will eventually aspire to be Google Scholar without the Google. It's deployed to Heroku for now.

### Sources
* The latest tables of contents from journals via [JournalTOCs](http://www.journaltocs.ac.uk/develop.php)
* [CrossRef REST API](https://github.com/CrossRef/rest-api-doc/blob/master/rest_api.md)

All sources are free and require no authentication to use the API.

### Example usage

This gets the latest articles, books, monographs, and book chapters with the word 'putin' in the title, sorted by date, with most recent first, published since March 2016.

http://scholarboteu.herokuapp.com/v1?date=2016-03&words=putin

http://localhost:5000/v1?date=2016-03&words=putin

```
{
  "length": 38,
  "results": [
    {
      "date": "2016-06-02",
      "source": "crossref",
      "title": "New trends in Russian political mentality: Putin 3.0",
      "type": "journal-article",
      "url": "http://dx.doi.org/10.5860/choice.197096"
    },
    {
      "date": "2016-05-26",
      "source": "crossref",
      "title": "La memoria dell'Urss nella Russia di Putin Manuali per l'universit\u00e0",
      "type": "journal-article",
      "url": "http://dx.doi.org/10.3280/pass2016-098006"
    },
    {
      "date": "2016-05-24",
      "source": "crossref",
      "title": "Khodorkovsky, Yukos, and Putin: The Achievement of Khodorkovsky, Why It Was Destroyed, and the Consequences",
      "type": "journal-article",
      "url": "http://dx.doi.org/10.1080/10758216.2016.1146859"
    },
  ...
  ]
}
```

The state machine and channel management is done using [RapidPro](https://github.com/rapidpro/rapidpro).
