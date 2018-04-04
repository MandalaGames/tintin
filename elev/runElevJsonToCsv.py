import json
import sys 
from DataProcessors import ElevJsonToCsv

outputFilename = ""
try:
    filename = sys.argv[1]
    resolution = int(sys.argv[2])
    outputFilename = sys.argv[3]
except IndexError:
    print("usage: runElevJsonToCsv.py inFile resolution outFile")

with open(filename) as f:
    data = json.loads(f.read())

csvData = ElevJsonToCsv.jsonToCsv(data, resolution)

with open(outputFilename, 'w') as f:
    f.write(csvData)
