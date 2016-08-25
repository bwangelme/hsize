#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
import doctest
import filesize


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(filesize))
    return tests

if __name__ == '__main__':
    unittest.main()
