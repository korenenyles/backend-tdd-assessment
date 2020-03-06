#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

class Test_Echo(unittest.TestCase):
    def test_help(self):
        """ Running the program without arguments should show usage. """
    
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper1(self):
        args = ["-u", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEquals(result, "HELLO")

    def test_upper2(self):
        args = ["-upper", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.upper)
        result = echo.main(args)
        self.assertEquals(result, "HELLO")

    def test_lower1(self):
        args = ["-l", "heLLo"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEquals(result, "hello")
    
    def test_lower2(self):
        args = ["-lower", "heLLo"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.lower)
        result = echo.main(args)
        self.assertEquals(result, "hello")
    
    def test_title1(self):
        args = ["-t", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEquals(result, "Hello")
    
    def test_title2(self):
        args = ["-title", "hello"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.title)
        result = echo.main(args)
        self.assertEquals(result, "Hello")
    
    def test_all_three(self):
        args = ["-tul", "heLLo"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.all)
        result = echo.main(args)
        self.assertEquals(result, "HELLO")

    def test_two(self):
        args = ["-tl", "heLLo"]
        namespace = self.parser.parse_args(args)
        self.assertTrue(namespace.two)
        result = echo.main(args)
        self.assertEquals(result, "hello")
    
    def no_args(self):
        args = ["Hello!"]
        result = echo.main(args)
        self.assertEquals(result, 'Hello!')

if __name__ == '__main__':
    unittest.main()