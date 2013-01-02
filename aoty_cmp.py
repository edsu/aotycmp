#!/usr/bin/env python

import json
import time
import logging
from urllib import quote, urlopen, urlencode

import oauth2 as oauth

import config


def main():
    logging.basicConfig(filename="aoty_cmp.log", level=logging.INFO)
    aoty = json.loads(open("aoty_dedupe.json").read())
    for a in aoty:
        try:
            artist = a['artist']
            album = a['album']
            a['spotify'] = spotify(artist, album)
            a['rdio'] = rdio(artist, album)
            logging.info(a)
        except Exception, e:
            logging.exception(e)
        time.sleep(1)
    open("aoty_cmp.json", "w").write(json.dumps(aoty, indent=2))

def spotify(artist, album):
    q = '%s AND "%s"' % (artist, album)
    q = quote(q.encode('utf-8'))
    url = 'http://ws.spotify.com/search/1/album.json?q=' + q
    j = urlopen(url).read()
    response = json.loads(j)

    can_stream = False
    url = None

    for a in response['albums']:
        if a['name'] == album and spotify_artist(a, artist):
            url = a['href']
            if config.COUNTRY in a['availability']['territories'].split(' '):
                can_stream = True

    return {'can_stream': can_stream, 'url': url}

def spotify_artist(a, artist_name):
    for artist in a['artists']:
        if artist['name'] == artist_name: 
            return True
    return False

def rdio(artist, album):
    consumer = oauth.Consumer(config.RDIO_CONSUMER_KEY, 
                              config.RDIO_CONSUMER_SECRET)
    client = oauth.Client(consumer)
    q = {'method': 'search', 
         'query': ('%s %s' % (artist, album)).encode('utf-8'), 
         'types': 'Album'}
    j = client.request('http://api.rdio.com/1/', 'POST', urlencode(q))[1]
    response = json.loads(j)

    can_stream = False
    url = None
    for r in response['result']['results']:
        if r['name'] == album and r['artist']:
            url = "http://rdio.com" + r['url']
            if r['canStream'] == True:
                can_stream = True

    return {'can_stream': can_stream, 'url': url}
    

if __name__ == "__main__":
    main()
