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
        self.assertTrue(os.path.isfile('notes/%s.txt' % self.title))

    def test_note_content(self):
        saved_content = open('notes/%s.txt' % self.title).read()
        self.assertEqual(saved_content, self.content)


if __name__ == '__main__':
    unittest.main()