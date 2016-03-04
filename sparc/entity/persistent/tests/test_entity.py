import unittest
from doctest import DocTestSuite
from doctest import DocFileSuite

import sparc.entity.persistent

def test_suite():
    return unittest.TestSuite((
        DocFileSuite('entity.txt',
                     package=sparc.entity.persistent),))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')