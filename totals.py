#!/usr/bin/env python

import json

aoty = json.loads(open('aoty-cmp.json').read())

rdio = spotify = count = 0.0

for a in aoty:
    if not a.has_key('rdio'): continue

    if a['rdio']['can_stream']:
        rdio += 1
    if a['spotify']['can_stream']:
        spotify += 1
    count += 1

print "spotify: %i %i %0.2f" % (spotify, count, (spotify/count))
print "rdio: %i %i %0.2f" % (rdio, count, (rdio/count))

