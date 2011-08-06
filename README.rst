aotycmp is a hack to see what albums on Alf Eaton's `Albums of the Year (AOTY) <http://aoty.hubmed.org>`_ list of lists can be streamed from `Spotify <http://spotify.com>`_ and `Rdio <http://rdio.com>`_. The results are found in aoty.json.

The steps for reproducing the results stored in aotycmp.json are to:

    1. pip install -r requirements.pip
    2. cp config.py.orig config.py
    3. get a Rdio API Key and put credentials in config.py
    4. ./aoty.py # crawls aoty.hubmed.org and stores data in aoty.json
    5. ./aoty-dedupe.py # dedupes albums across lists and stores in aoty-dedupe.json
    6. ./aotycmp.py # reds aoty-dedupe.json and stores results of rdio/spotify lookups in aotycmp.json

Maybe I should've dumped the crawled data into CouchDB instead of chaining
JSON dumps together like this. Could be more fun right? It would make it
easier to not repeat spotify and rdio API lookups. 
