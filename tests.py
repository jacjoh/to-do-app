#!/usr/bin/env python3.6

import unittest
import app

class TestTODOApp(unittest.TestCase):
    def setUp(self):
        self.app = app.TODO()

    def test_setup(self):
        self.assertTrue(len(self.app.tasks) == 0)
    
    def test_adding(self):
        self.app.add("Adding a task")
        self.assertTrue(len(self.app.tasks) == 1)
        self.assertEqual(self.app.tasks[1], "Adding a task")

    def test_do(self):
        pass

if __name__ == '__main__':
    unittest.main()