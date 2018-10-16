#!/usr/bin/env python3.6

import unittest
import app

class TestTODOApp(unittest.TestCase):
    def setUp(self):
        self.app = app.TODO()

    def test_setup(self):
        self.assertTrue(len(self.app.tasks) == 0)
    
    def test_adding(self):
        self.app.add("")
        self.assertTrue(len(self.app.tasks) == 0)

        self.app.add("Adding a task")
        self.assertTrue(len(self.app.tasks) == 1)
        self.assertEqual(self.app.tasks['1'], "Adding a task")

        expected_result = """{"1": "Adding a task"}"""
        filename = 'backup.txt'

        with open(filename, 'r') as f:
            read_data = f.read()

        self.assertEqual(expected_result, read_data)   
 

    def test_do(self):
        self.app.add("Adding a Task")

        self.app.do("#2")
        self.assertTrue(len(self.app.tasks) == 1)

        self.app.do("")
        self.assertTrue(len(self.app.tasks) == 1)

        self.app.do("Adding a Task")
        self.assertTrue(len(self.app.tasks) == 1)

        self.app.do("#1")
        self.assertTrue(len(self.app.tasks) == 0)
        
        expected_result = """{}"""
        filename = "backup.txt"

        with open(filename, 'r') as f:
            read_data = f.read()

        self.assertEqual(expected_result, read_data)


if __name__ == '__main__':
    unittest.main()