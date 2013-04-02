#!/usr/bin/env python

import re
import sys
import json
import time
import logging
from urllib import quote, urlopen, urlencode

import oauth2 as oauth

import config


def main(console=False):
    logging.basicConfig(filename="aoty_cmp.log", level=logging.INFO)
    aoty = json.loads(open("aoty_dedupe.json").read())
    for a in aoty:
        try:
            artist = a['artist']
            album = a['album']
            a['spotify'] = spotify(artist, album)
            a['rdio'] = rdio(artist, album)
            if console:
                progress(a)
            logging.info(a)
        except Exception, e:
            logging.exception(e)
            sys.exit()
        time.sleep(1)
    open("aoty_cmp.json", "w").write(json.dumps(aoty, indent=2))

def spotify(artist, album):
    q = '%s AND "%s"' % (artist, album)
    q = quote(q.encode('utf-8'))
    url = 'http://ws.spotify.com/search/1/album.json?q=' + q

    # spotify search api throws sporadic 502 errors
    tries = 0
    max_tries = 10
    response = None
    while True:
        tries += 1
        r = urlopen(url)

        if r.code == 200:
            j = urlopen(url).read()
            response = json.loads(r.read())
            break

        if tries > max_tries: 
            break

        backoff = tries ** 2 
        logging.warn("received %s when fetching %s, sleeping %s", r.code, url, backoff)
        time.sleep(backoff)

    if not response:
        raise Exception("couldn't talk to Spotify for %s/%s", artist, album)

    can_stream = False
    url = None

    for a in response['albums']:
        if a['name'].lower() == album.lower() and spotify_artist(a, artist):
            url = a['href']
            if config.COUNTRY in a['availability']['territories'].split(' ') or a['availability']['territories'] == 'worldwide': 
                can_stream = True

    return {'can_stream': can_stream, 'url': url}

def spotify_artist(a, artist_name):
    for artist in a['artists']:
        if clean(artist['name']) == clean(artist_name): 
            return True
    return False

def rdio(artist, album):
    consumer = oauth.Consumer(config.RDIO_CONSUMER_KEY, 
                              config.RDIO_CONSUMER_SECRET)
    client = oauth.Client(consumer)
    q = {
        'method': 'search', 
        'query': ('%s %s' % (artist, album)).encode('utf-8'), 
        'types': 'Album',
        '_region': config.COUNTRY
    }
    j = client.request('http://api.rdio.com/1/', 'POST', urlencode(q))[1]
    try: 
        response = json.loads(j)
    except: 
        logging.error("unable to load json from %s: %s", url, j)

    can_stream = False
    url = None
    for r in response['result']['results']:
        if clean(r['name']) == clean(album) and clean(r['artist']) == clean(artist):
            url = "http://rdio.com" + r['url']
            if r['canStream'] == True:
                can_stream = True

    return {'can_stream': can_stream, 'url': url}

def progress(a):
    r = a['rdio']['can_stream']
    s = a['spotify']['can_stream']
    if r and s:
        sys.stderr.write(".")
    elif r:
        sys.stderr.write("r")
    elif s:
        sys.stderr.write("s")
    else:
        sys.stderr.write("x")

def clean(a):
    a = a.lower()
    a = re.sub('^the ', '', a)
    a = re.sub(' \(.+\)$', '', a)
    return a

if __name__ == "__main__":
    main(console=True)
