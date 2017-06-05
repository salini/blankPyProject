
import common  # to load path to myProject package

import unittest

import myProject

class Test00Case(unittest.TestCase):

    def test_simpleFunction(self):
        self.assertTrue(myProject.returnTrueFunction())


if __name__ == "__main__":
    print "end of test00 script"