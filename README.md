aotycmp
=======

aotycmp is a hack to see what albums on Alf Eaton's `Albums of the Year (AOTY) <http://aoty.hubmed.org>`_ list of lists can be streamed from `Spotify <http://spotify.com>`_ and `Rdio <http://rdio.com>`_.

If you just want to see the current results take a look at the line-oriented
aoty.json file.

The steps for reproducing the results can be done using the following steps:

    pip install -r requirements.pip
    cp config.py.orig config.py
    # add rdio keys to config.py
    ./aoty.py | ./compare.py > aoty.json

Maybe I should have dumped the crawled data into CouchDB instead of chaining
JSON dumps together like this. Could be more fun right? It would make it
easier to not repeat spotify and rdio API lookups. 

If you have your own list of albums, and you want to see if they are available
on spotify and rdio, you should be able to format your list like
aoty_dedupe.json and point aoty_cmp.py at it. 

Alf says, it might be easier to scrape the content using this URL in the future:
http://apps.hubmed.org/aoty/?_start=0&_limit=1000&_format=xml
