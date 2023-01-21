#!/usr/bin/env python

"""
Author: Nick Russo
File: shape_unittest.py
Purpose: Entrypoint for unittest regression testing of the
circle and rectangle classes.
"""

import unittest
from unittests.rectangle_test import RectangleTest
from unittests.circle_test import CircleTest
from unittests.triangle_test import TriangleTest


def main():
    """
    Test execution starts here.
    """

    # The loader is responsible for loading test cases into test suites
    test_loader = unittest.TestLoader()

    # Build a list of test suites to run
    test_suites = [
        test_loader.loadTestsFromTestCase(CircleTest),
        test_loader.loadTestsFromTestCase(RectangleTest),
        test_loader.loadTestsFromTestCase(TriangleTest),
    ]

    # The runner is responsible for executing tests and printing outputs
    test_runner = unittest.TextTestRunner(verbosity=2)

    # Iterate over all of the test suites, run each one in series
    for test_suite in test_suites:
        test_runner.run(test_suite)


if __name__ == "__main__":
    main()
