import os
import unittest

import pynotes


class AddTest(unittest.TestCase):

    def setUp(self):
        self.title = 'test'
        self.content = """
            test content
            hello
            hello
            test"""
        pynotes.add_note(self.title, self.content)

    def test_added_note_exists(self):
        self.assertTrue(os.isfile('notes/%s.txt' % self.title))