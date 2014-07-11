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

    def tearDown(self):
        os.remove('notes/%s.txt' % self.title)

    def test_note_exists(self):
        self.assertTrue(os.path.isfile('notes/%s.txt' % self.title))

    def test_note_content(self):
        saved_content = open('notes/%s.txt' % self.title).read()
        self.assertEqual(saved_content, self.content)


class DeleteTest(unittest.TestCase):

    def setUp(self):
        self.title = 'test'
        self.content = 'whatever'
        pynotes.add_note(self.title, self.content)
        pynotes.delete_note(self.title)

    def test_note_doesnt_exist(self):
        self.assertFalse(os.path.exists('notes/%s.txt' % self.title))


if __name__ == '__main__':
    unittest.main()