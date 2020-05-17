#!/usr/bin/env python3


class Parser:
    def __init__(self, data):
        self.data = data
        self.currPos = 0

    def peek(self):
        return self.data[self.currPos]

    def peekNext(self):
        if len(data) < self.currPos + 1:
            return self.data[self.currPos + 1]
        return ""

    def consume(self, char):
        if self.data[self.currPos] == char:
            self.currPos += 1
            return True
        return False

    def consumeWhiteSpace(self):
        length = len(self.data)
        while self.data[self.currPos].isspace():
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
        while self.currPos < length:
            if self.data[self.currPos] == '"':
                break
            self.currPos += 1
        return self.data[start : self.currPos]

    def parseNumber(self):
        length = len(self.data)
        start = self.currPos
        while self.currPos < length:
            if not self.data[self.currPos].isdigit and (not (self.data[self.currPos] == ".")) and (not (self.data[self.currPos]== "-")):
                break
            self.currPos += 1
        return self.data[start : self.currPos]
