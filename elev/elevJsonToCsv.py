import json
import sys 
import JsonToCsv

outputFilename = ""
try:
    filename = sys.argv[1]
    resolution = int(sys.argv[2])
    outputFilename = sys.argv[3]
except IndexError:
    print("usage: elevJsonToCsv.py inFile resolution outFile")

with open(filename) as f:
    data = json.loads(f.read())

csvData = JsonToCsv.jsonToCsv(data, resolution)

with open(outputFilename, 'w') as f:
    f.write(csvData)
