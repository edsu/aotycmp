#!/usr/bin/env python

"""
Reads Alf's AOTY website and writes out line-oriented json, one line for 
each unique album in the list of lists.
"""

import json

from lxml import html


def main():
    aoty = {}
    for y in [2007, 2008, 2009, 2010, 2011, 2012]:
        aoty[y] = list(year(y))
    aoty = dedupe(aoty)
    for album in aoty:
        print json.dumps(album)

def year(y):
    start = 0
    while start != None:
        url = 'http://apps.hubmed.org/aoty/%i?_start=%i' % (y, start)
        doc = html.parse(url)
        for a in album_lists(doc):
            yield a
        if doc.xpath(".//a[@rel='next']"):
            start += 20
        else:
            start = None

def album_lists(doc):
    for album_list in doc.xpath(".//div[@class='item']"):
        a = album_list.xpath(".//a[@class='title']")[0]
        list_name = a.text
        list_url = a.attrib['href']
        yield {'name': list_name,
                'url': list_url, 
                'albums': list(albums(album_list))}

def albums(doc):
    for album in doc.xpath(".//li[@class='album haudio']"):
        artist = album.xpath("string(a[@class='artist contributor'])")
        album_title = album.xpath("string(a[@class='title album'])")
        yield {'artist': artist, 'album': album_title}

def dedupe(aoty):
    albums = {}
    album_counts = {}

    for year in aoty.keys():
        for album_list in aoty[year]:
            for album in album_list['albums']:
                k = "%(artist)s :~: %(album)s" % album
                albums[k] = album
                album_counts[k] = album_counts.get(k, 0) + 1

    album_keys = albums.keys()
    album_keys.sort(lambda a, b: cmp(album_counts[b], album_counts[a]))

    sorted_albums = []
    for k in album_keys:
        album = albums[k]
        album['listed'] = album_counts[k]
        sorted_albums.append(album)

    return sorted_albums

if __name__ == "__main__":
    main()
