import os
import unittest

import pynotes


class AddTest(unittest.TestCase):

    def setUp(self):
        self.title = 'test'
        pynotes.add(self.title)

    def tearDown(self):
        os.remove('notes/%s.txt' % self.title)

    def test_note_exists(self):
        self.assertTrue(os.path.isfile('notes/%s.txt' % self.title))


class DeleteTest(unittest.TestCase):

    def setUp(self):
        self.title = 'test'
        self.content = 'whatever'
        pynotes.add(self.title)
        pynotes.delete(self.title)

    def test_note_doesnt_exist(self):
        self.assertFalse(os.path.exists('notes/%s.txt' % self.title))


if __name__ == '__main__':
    unittest.main()