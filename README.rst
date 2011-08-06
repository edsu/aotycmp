aotycmp is a hack to see what listed on Alf Eaton's [Albums of the
Year](http://aoty.hubmed.org) list of lists (AOTY) can be found and 
streamable in Spotify and Rdio. The results are found in aoty.json.

The steps for reproducing the aoty.json are to:

  1. pip install -r requirements.pip
  1. cp config.py.orig config.py
  1. get a Rdio API Key and put credentials in config.py
  1. ./aoty.py # crawls aoty.hubmed.org and stores data in aoty.json
  1. ./aoty-dedupe.py # dedupes albums across lists and stores in aoty-dedupe.json
  1. ./aotycmp.py # reds aoty-dedupe.json and stores results of rdio/spotify lookups in aotycmp.json

Maybe I should've dumped the crawled data into CouchDB instead of chaining
JSON dumps together like this. Could be more fun right? It would make it
easier to not repeat spotify and rdio API lookups. 
