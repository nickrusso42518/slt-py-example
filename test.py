'''
Author: Nick Russo
File: test.py
Purpose: Entrypoint for unittest regression testing of the
circle and rectangle classes.
'''

import unittest
from shapetests.rectangle_test import RectangleTest
from shapetests.circle_test import CircleTest

def main():
    '''
    Test execution starts here.
    '''

    # The loader is responsible for loading test cases into test suites
    test_loader = unittest.TestLoader()

    # Build a list of test suites to run
    test_suites = [
        test_loader.loadTestsFromTestCase(CircleTest),
        test_loader.loadTestsFromTestCase(RectangleTest)
    ]

    # The runner is responsible for executing tests and printing output
    test_runner = unittest.TextTestRunner(verbosity=2)

    # Iterate over all of the test suites, run each one in series
    for test_suite in test_suites:
        test_runner.run(test_suite)

if __name__ == '__main__':
    main()
