#!/usr/bin/env python

# potentially useful for dumping the data for a spreadsheet

import csv
import json

writer = csv.writer(open('aoty_cmp.csv', 'w'), dialect='excel')
writer.writerow(["Artist", "Album", "Listed", "Spotify URL", 
    "Spotify Streamable", "Rdio URL", "Rdio Streamable"])

for a in json.loads(open('aoty_cmp.json').read()):
    if not a.has_key('spotify') or not a.has_key('rdio'):
        continue
    row = [a['artist'].encode('utf-8'),
           a['album'].encode('utf-8'),
           a['listed'],
           a['spotify']['url'],
           a['spotify']['can_stream'],
           a['rdio']['url'],
           a['rdio']['can_stream']]
    writer.writerow(row)


