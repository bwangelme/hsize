#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest, doctest


# def test_suite():
#     return unittest.TestSuite((
#         doctest.DocTestSuite('filesize')
#     ))

unittest.TestSuite((doctest.DocTestSuite('filesize')))

if __name__ == '__main__':
    unittest.main()
