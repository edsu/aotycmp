aotycmp
=======

aotycmp is a hack to see what albums on Alf Eaton's `Albums of the Year (AOTY) <http://aoty.hubmed.org>`_ list of lists can be streamed from `Spotify <http://spotify.com>`_ and `Rdio <http://rdio.com>`_.

There are a few JSON data files in this repository:

    * aoty.json - the full dump af AOTY scraped data
    * aoty-dedupe.json - the albums aggregated together 
    * aoty-cmp.json - the results of looking up albums at rdio and spotify

The steps for reproducing the results stored in aoty-cmp.json are to:

    1. pip install -r requirements.pip
    2. cp config.py.orig config.py
    3. get a Rdio API Key and put credentials in config.py
    4. ./aoty.py # crawls aoty.hubmed.org and stores data in aoty.json
    5. ./aoty-dedupe.py # dedupes albums across lists and stores in aoty-dedupe.json
    6. ./aoty-cmp.py # reads aoty-dedupe.json and stores results of rdio/spotify lookups in aoty-cmp.json
    7. ./aoty-csv.py # dump aoty-cmp.json as csv for spreadsheet

Maybe I should've dumped the crawled data into CouchDB instead of chaining
JSON dumps together like this. Could be more fun right? It would make it
easier to not repeat spotify and rdio API lookups. 

If you have your own list of albums, and you want to see if they are available
on spotify and rdio, you should be able to create your own JSON file including
basically a list of albums:

    [
      {
        "album": "Movement',
        "artist": "New Order"
      }
      ...
    ]

And feed it to aoty-cmp.py...
