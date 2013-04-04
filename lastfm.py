#!/usr/bin/env python

"""
Reads the line oriented output of compare.py and layers in last.fm information
where available. You'll need to add your lastfm key to config.py
"""

import sys
import json
import time
import config
import logging
import requests
import fileinput

def main():
    logging.basicConfig(filename="lastfm.log", level=logging.INFO)
    for line in fileinput.input():
        a = json.loads(line)
        info = lastfm(a["artist"], a["album"])
        if not info:
            logging.warn("no hit for %s/%s", artist, album)
        else:
            logging.info("found %s" % info["album"]["url"])
            a["lastfm"] = info["album"]
        print json.dumps(a)
        # TODO: make this configurable
        time.sleep(1)

def lastfm(artist, album):
    url = 'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key=%s&artist=%s&album=%s&format=json'
    r = requests.get(url % (config.LASTFM_KEY, artist, album))
    if r.status_code == 200:
        return json.loads(r.content)
    else:
        logging.warn("got %s when fetching info for %s/%s", (r.status_code, artist, album))
    return None

if __name__ == "__main__":
    main()
