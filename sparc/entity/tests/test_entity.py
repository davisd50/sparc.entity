import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.entity

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('entity.txt',
                     package=sparc.entity),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')