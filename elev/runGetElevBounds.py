import json
import sys 
import getElevBounds

outputFilename = ""
try:
    filename = sys.argv[1]

except IndexError:
    print("usage: runGetElevBounds tifFilename")

getElevBounds.getGdalInfo(filename)
