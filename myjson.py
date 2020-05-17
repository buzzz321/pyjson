#!/usr/bin/env python3

from enum import Enum


class JType(Enum):
    JString = 1
    JNumber = 2
    JObject = 3
    JArray = 4
    Undef = 0


class JValue:
    def __init__(self, type=JType.Undef, value=None):
        self.type = type
        self.value = value

    def __str__(self):
        return "[%s, %s]" % (self.type, self.value)

    def __repr__(self):
        return "[%s, %s]" % (self.type, self.value)

    def getValue(self):
        return self.value

    def getType(self):
        return self.type


class JSObject:
    def __init__(self, key=None, value=None):
        self.data = {}
        if key is not None:
            self.data[key] = value

    def __str__(self):
        return "%s" % (self.data)

    def add(self, key, value):
        self.data[key] = value


class Parser:
    def __init__(self, data):
        self.data = data
        self.currPos = 0

    def peek(self):
        if self.currPos < len(self.data):
            return self.data[self.currPos]
        return ""

    def peekNext(self):
        if self.currPos + 1 < len(self.data):
            return self.data[self.currPos + 1]
        return ""

    def consume(self, char):
        if (self.currPos < len(self.data)) and (self.data[self.currPos] == char):
            self.currPos += 1
            return True
        return False

    def consumeWhiteSpace(self):
        length = len(self.data)

        while self.currPos < length:
            if not self.data[self.currPos].isspace():
                return True
            self.currPos += 1
            if self.currPos >= length:
                self.currPos -= 1
                return False
        return True

    def parseQuotedString(self):
        length = len(self.data)
        if not self.consume('"'):
            return ""  # start not found so return empty string
        start = self.currPos
        while self.currPos < length and self.data[self.currPos] != '"':
            self.currPos += 1

        self.consume('"')
        return self.data[start : self.currPos - 1]

    def parseNumber(self):
        length = len(self.data)
        start = self.currPos
        while self.currPos < length:
            if self.data[self.currPos].isdigit():
                self.currPos += 1
            elif (self.data[self.currPos] == ".") or (self.data[self.currPos] == "-"):
                self.currPos += 1
            else:
                break

        return self.data[start : self.currPos]

    def parseObject(self):
        length = len(self.data)
        retVal = JSObject()
        key = ""
        value = JSObject("", JValue(0, ""))
        self.consume("{")

        while True:
            self.consumeWhiteSpace()
            if self.consume("}"):
                return retVal

            key = self.parseQuotedString()
            self.consumeWhiteSpace()
            self.consume(":")
            value = self.parseValue()
            retVal.add(key, value)
            # print(retVal)
            self.consumeWhiteSpace()
            self.consume(",")

    def parseValue(self):
        self.consumeWhiteSpace()

        ch = self.peek()

        if ch == "{":
            obj = self.parseObject()
            return JValue(JType.JObject, obj)
        elif ch == "[":
            arr = self.parseArray()
            return JValue(JType.JArray, arr)
        elif ch.isdigit():
            number = self.parseNumber()
            return JValue(JType.JNumber, number)
        elif ch == '"':
            strVal = self.parseQuotedString()
            return JValue(JType.JString, strVal)
        else:
            print("ch=" + str(ch) + "|")
            raise Exception("Unknown value type. ")
