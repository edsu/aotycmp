#!/usr/bin/env python

"""
calculates summary totals given the output of compare.py
"""

import json
import fileinput

rdio = spotify = count = 0.0

for line in fileinput.input():
    a = json.loads(line)
    if not a.has_key('rdio'): continue

    if a['rdio']['can_stream']:
        rdio += 1
    if a['spotify']['can_stream']:
        spotify += 1
    count += 1

print "spotify: %i %i %0.2f" % (spotify, count, (spotify/count))
print "rdio: %i %i %0.2f" % (rdio, count, (rdio/count))

