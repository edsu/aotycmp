aotycmp
=======

aotycmp is a hack to see what albums on Alf Eaton's `Albums of the Year (AOTY) <http://aoty.hubmed.org>`_ list of lists can be streamed from `Spotify <http://spotify.com>`_ and `Rdio <http://rdio.com>`_.

There are a few JSON data files in this repository:

* aoty.json - the full dump af AOTY scraped data
* aoty_dedupe.json - the albums aggregated together 
* aoty_cmp.json - the results of looking up albums at rdio and spotify
* aoty_cmp.csv - results suitable for import to a spreadsheet

The steps for reproducing the results stored in aoty_cmp.json are to:

#. pip install -r requirements.pip
#. cp config.py.orig config.py
#. get a Rdio API Key and put credentials in config.py
#. ./aoty.py # crawls aoty.hubmed.org and stores data in aoty.json
#. ./aoty_dedupe.py # dedupes albums across lists and stores in aoty_dedupe.json
#. ./aoty_cmp.py # reads aoty_dedupe.json and stores results of rdio/spotify lookups in aoty_cmp.json
#. ./aoty_csv.py # dump aoty_cmp.json as csv for spreadsheet

Maybe I should've dumped the crawled data into CouchDB instead of chaining
JSON dumps together like this. Could be more fun right? It would make it
easier to not repeat spotify and rdio API lookups. 

If you have your own list of albums, and you want to see if they are available
on spotify and rdio, you should be able to format your list like
aoty_dedupe.json and point aoty_cmp.py at it. 

Alf says, it might be easier to scrape the content using this URL in the future:
http://apps.hubmed.org/aoty/?_start=0&_limit=1000&_format=xml
