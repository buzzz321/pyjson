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
        uat = Parser("123")
        result = uat.parseNumber()
        self.assertEqual("123", result)

    def test_parseFractionalNumber(self):
        uat = Parser("123.4")
        result = uat.parseNumber()
        self.assertEqual("123.4", result)

    def test_parseNegativeFractionalNumber(self):
        uat = Parser("-123.4")
        result = uat.parseNumber()
        self.assertEqual("-123.4", result)

    def test_parseSimpleObject(self):
        uat = Parser('{ "nyckel" : "värde" }')
        result = uat.parseObject()

        self.assertEqual("nyckel", list(result.data)[0])
        self.assertEqual("värde", result.data["nyckel"].getValue())
        self.assertEqual(JType.JString, result.data["nyckel"].getType())

    def test_parseMultiElementObject(self):
        uat = Parser('{ "red" : 1, "green" : 2, "yellow": 3 }')
        result = uat.parseObject()

        self.assertEqual("red", list(result.data)[0])
        self.assertEqual("1", result.data["red"].getValue())
        self.assertEqual(JType.JNumber, result.data["red"].getType())

        self.assertEqual("green", list(result.data)[1])
        self.assertEqual("2", result.data["green"].getValue())
        self.assertEqual(JType.JNumber, result.data["green"].getType())

        self.assertEqual("yellow", list(result.data)[2])
        self.assertEqual("3", result.data["yellow"].getValue())
        self.assertEqual(JType.JNumber, result.data["yellow"].getType())

    def test_parseSimpleArray(self):
        uat = Parser('[1,2,3,4,5]')
        result = uat.parseArray()

        #print(result)
        self.assertEqual("1", result[0].getValue())
        self.assertEqual(JType.JNumber, result[0].getType())

    def test_parseArray(self):
        uat = Parser('{ "arr": [10,20,30,40,50]}')
        result = uat.parseObject()

        #print(result)
        self.assertEqual("arr", list(result.data)[0])
        self.assertEqual(JType.JArray, result.data["arr"].getType())
        self.assertEqual(JType.JNumber,
                         result.data["arr"].getValue()[0].getType())


if __name__ == "__main__":
    unittest.main()
