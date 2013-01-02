#!/usr/bin/env python

import json

from lxml import html


def main():
    aoty = {}
    for y in [2007, 2008, 2009, 2010, 2011, 2012]:
        aoty[y] = list(year(y))
    open("aoty.json", "w").write(json.dumps(aoty, indent=2))

def year(y):
    start = 0
    while start != None:
        url = 'http://apps.hubmed.org/aoty/%i?_start=%i' % (y, start)
        doc = html.parse(url)
        print url
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

if __name__ == "__main__":
    main()
