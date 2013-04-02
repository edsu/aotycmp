#!/usr/bin/env python

from aoty_cmp import rdio, spotify, clean

import unittest

class Tests(unittest.TestCase):
    
    def test_rdio(self):
        i = rdio('Radiohead', 'In Rainbows')
        self.assertEqual(i['can_stream'], True)
        self.assertEqual(i['url'], 'http://rdio.com/artist/Radiohead/album/In_Rainbows/')

    def test_spotify(self):
        i = spotify('Velvet Underground', 'Loaded')
        self.assertEqual(i['can_stream'], True)
        self.assertEqual(i['url'], 'spotify:album:4BOaL1TOarypViTKNrcP8d')

    def test_clean(self):
        self.assertEqual(clean("Bar Fighters"), "barfighters")
        self.assertEqual(clean("Third (Non EU Version)"), "third")
        self.assertEqual(clean("Thriller."), "thriller")
        self.assertEqual(clean("The Fixx"), "fixx")
        self.assertEqual(clean("The Good and the Bad"), "goodthebad")

if __name__ == "__main__":
    unittest.main()
