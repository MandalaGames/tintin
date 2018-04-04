import os

class CsvReader(object):
    def __init__(self, filename, datatypes, maxSize = 0):
        self.filename = filename
        self.datatypes = datatypes 
        self.maxSize = maxSize

    def getGrid(self):
        with open(self.filename) as f:
            lines = f.readlines()
        out = []
        for line in lines:
            outLine = []
            for i,item in enumerate(line.split(",")):
                outLine.append(self.datatypes[i](item)) 
            out.append(outLine)
        return out
