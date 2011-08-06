#!/usr/bin/env python

import json

aoty = json.loads(open('aoty.json').read())

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

open('aoty-dedupe.json', 'w').write(json.dumps(sorted_albums, indent=2))



    

