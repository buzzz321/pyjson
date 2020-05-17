import unittest
from myjson import *

class TestMyJsonMethods(unittest.TestCase):

    def test_comsumeWhiteSpace(self):
        uat = Parser("   \n\t  werp")
        uat.consumeWhiteSpace()
        self.assertEqual("werp", uat.data[uat.currPos:])

    def test_parseQuotedString(self):
        uat = Parser('"key":')
        result = uat.parseQuotedString()
        self.assertEqual("key", result)

    def test_parseNumber(self):
        uat = Parser('123')
        result = uat.parseNumber()
        self.assertEqual("123", result)

    def test_parseFractionalNumber(self):
        uat = Parser('123.4')
        result = uat.parseNumber()
        self.assertEqual("123.4", result)

    def test_parseNegativeFractionalNumber(self):
        uat = Parser('-123.4')
        result = uat.parseNumber()
        self.assertEqual("-123.4", result)



if __name__ == '__main__':
    unittest.main()
